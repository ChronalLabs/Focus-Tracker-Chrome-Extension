from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from datetime import date, timedelta
from ..models import ActivityLog, UserStreak
from ..utils.focus_utils import calculate_focus_score, generate_suggestion
from schemas import FocusScoreResponse
from collections import defaultdict

router = APIRouter(
    prefix="/focus-score", tags=["focus-score"]
)

from datetime import date, timedelta

def update_streak(db: Session, user_id: str, today_score: float) -> int:
    """
    Updates and returns the user's current streak based on today's score.
    A valid streak day requires today_score >= 70.
    """

    # 1. Get today's and yesterday's date (use date objects, not strings)
    today = date.today()
    yesterday = today - timedelta(days=1)

    # 2. Fetch existing streak record
    streak = db.query(UserStreak).filter(UserStreak.user_id == user_id).first()

    # 3. If no record exists → create one
    if not streak:
        streak = UserStreak(
            user_id=user_id,
            streak_days=0,
            last_focus_date=None
        )
        db.add(streak)

    # 4. If today's score meets the minimum requirement
    if today_score >= 70:

        # Case A: Already updated today → do nothing (avoid double counting)
        if streak.last_focus_date == today:
            pass

        # Case B: Yesterday was last active → continue streak
        elif streak.last_focus_date == yesterday:
            streak.streak_days += 1
            streak.last_focus_date = today

        # Case C: First time OR streak broken → restart
        else:
            streak.streak_days = 1
            streak.last_focus_date = today

    else:
        # Case D: Score below threshold → break streak (strict logic)
        # Only reset if user hasn't already logged today
        if streak.last_focus_date != today:
            streak.streak_days = 0

    # 5. Save changes to database
    db.commit()

    # 6. Refresh object (ensures latest DB state)
    db.refresh(streak)

    # 7. Return updated streak count
    return streak.streak_days



@router.get("/", response_model=FocusScoreResponse)
def get_focus_score(user_id:str= "default_user", db: Session = Depends(get_db)):
    today = date.today()
    logs = ( 
        db.query(ActivityLog).filter(ActivityLog.user_id==user_id, func.date(ActivityLog.timestamp)==today).all()
    )

    productive = sum(l.duration for l in logs if l.category == "productive")
    distracting = sum(l.duration for l in logs if l.category == "distracting")
    neutral = sum(l.duration for l in logs if l.category == "neutral")

    total = productive + neutral + distracting 
    score = calculate_focus_score(productive, total)


    # for distracting sites: 
    distracting_sites = defaultdict(float)
    for log in logs: 
        if log.category == "distracting":
            distracting_sites[log.domain] += log.duration 
    

    top_distracting = sorted(
        distracting_sites.keys(),
        key=lambda d: distracting_sites[d], # Sort based on the value (time spent), not the key
        reverse=True
    )

    streak_days= update_streak(db, user_id, score)
    suggestions = generate_suggestion(score, distracting, top_distracting, streak_days)


    return FocusScoreResponse(
        focus_score=score,
        productive_time= productive,
        neutral_time=neutral,
        distractive_time=distracting,
        total_time=total,
        streak_days = streak_days,
        suggestions=suggestions,
    )

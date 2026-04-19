from pydantic import BaseModel
from typing import Optional 
from datetime import datetime


# Class - 1: 
class ActivityCreate(BaseModel):
    user_id: Optional[str]="default_user" 
    # By marking user_id as Optional[str], 
    # you are telling the program that a value for this field is not 
    # strictly required when a new object is created.
    url:str
    duration: float

  # ActivityCreate → “I receive clean JSON” → no config needed
  # ActivityResponse → “I receive messy objects” → config needed

class ActivityResponse(BaseModel):
    id:int
    user_id:str
    url:str
    domain:str
    duration: float
    category: str
    timestamp: datetime
         
    # Without Config → “I only understand JSON/dict”
    # With from_attributes=True → “I can also understand Python objects”
    class Config:
        form_attribute=True
    # Use Config (from_attributes) ONLY when working with ORM/database objects
    # Don’t use it for request models (unless special cases)    
  

class SiteCategoryCreate(BaseModel):
    domain: str
    category: str
# categorizes sites into neutral, productive, or distractive
    
class SiteCategoryResponse(BaseModel):
    id: int
    domain: str
    category: str
    is_custom: bool

    class Config:
        form_attribute=True

class FocusScoreResponse(BaseModel):
    focus_score: float
    productive_time: float
    distractive_time: float
    neutral_time: float
    total_time: float
    streak_days: int
    suggestions: str

class DomainStat(BaseModel):
    domain:str
    total_time:float
    percentage:float
    category:str

class DailyReportResponse(BaseModel):
    date: str
    focus_score: float
    productive_time: float
    distractive_time: float
    neutral_time: float
    total_time: float
    top_sites: list[DomainStat]
    hourly_activity: dict

class WeeklyReportResponse(BaseModel):
    week_start: str
    week_end: str
    average_focus_score: float 
    total_time:float
    daily_score: dict
    top_distracting_sites: list[DomainStat]
    top_productive_sites: list[DomainStat]
    
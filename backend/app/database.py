from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL="sqlite:///./focus_tracker.db" # initialized database name

# Initialise engine:
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={ "check_same_thread" : False },
)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

base=declarative_base()

# define database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
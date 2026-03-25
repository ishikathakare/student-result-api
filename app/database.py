from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# This creates the connection to MySQL
engine = create_engine(DATABASE_URL)

# Each request gets its own database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All our models will inherit from this
Base = declarative_base()

# This function gives a DB session to each API request and closes it after
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
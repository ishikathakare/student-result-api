from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --- User Schemas ---
class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# --- Student Schemas ---
class StudentCreate(BaseModel):
    name: str
    email: str
    branch: str
    year: int

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    branch: str
    year: int

    class Config:
        from_attributes = True

# --- Result Schemas ---
class ResultCreate(BaseModel):
    subject: str
    marks: float
    grade: str
    student_id: int

class ResultResponse(BaseModel):
    id: int
    subject: str
    marks: float
    grade: str
    student_id: int

    class Config:
        from_attributes = True
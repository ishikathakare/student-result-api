from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    branch = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)

    # One student can have many results
    results = relationship("Result", back_populates="student")

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(100), nullable=False)
    marks = Column(Float, nullable=False)
    grade = Column(String(5), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    # Link back to student
    student = relationship("Student", back_populates="results")
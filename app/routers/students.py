from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter(prefix="/students", tags=["Students"])

# Add a new student
@router.post("/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Check if email already exists
    existing = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Get all students
@router.get("/", response_model=list[schemas.StudentResponse])
def get_all_students(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(models.Student).all()

# Get one student by ID
@router.get("/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update student
@router.put("/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, updated: schemas.StudentCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    for key, value in updated.dict().items():
        setattr(student, key, value)
    
    db.commit()
    db.refresh(student)
    return student

# Delete student
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}
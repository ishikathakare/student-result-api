from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter(prefix="/results", tags=["Results"])

# Add result for a student
@router.post("/", response_model=schemas.ResultResponse)
def add_result(result: schemas.ResultCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Check if student exists
    student = db.query(models.Student).filter(models.Student.id == result.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    new_result = models.Result(**result.dict())
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result

# Get all results for a student
@router.get("/{student_id}", response_model=list[schemas.ResultResponse])
def get_results(student_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    results = db.query(models.Result).filter(models.Result.student_id == student_id).all()
    if not results:
        raise HTTPException(status_code=404, detail="No results found for this student")
    return results

# Update a result
@router.put("/{result_id}", response_model=schemas.ResultResponse)
def update_result(result_id: int, updated: schemas.ResultCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    result = db.query(models.Result).filter(models.Result.id == result_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    
    for key, value in updated.dict().items():
        setattr(result, key, value)
    
    db.commit()
    db.refresh(result)
    return result

# Delete a result
@router.delete("/{result_id}")
def delete_result(result_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    result = db.query(models.Result).filter(models.Result.id == result_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    
    db.delete(result)
    db.commit()
    return {"message": "Result deleted successfully"}
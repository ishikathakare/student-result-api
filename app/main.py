from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import engine, get_db, Base
from app import models, schemas
from app.auth import hash_password, verify_password, create_access_token
from app.routers import students, results

# This auto-creates all tables in MySQL on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Result Management API")

# Include routers
app.include_router(students.router)
app.include_router(results.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Student Result Management API is running!"}

# Register a new user
@app.post("/auth/register", response_model=schemas.Token)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = models.User(
        username=user.username,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()

    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# Login
@app.post("/auth/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
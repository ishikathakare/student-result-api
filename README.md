# Student Result Management API

A REST API built with **FastAPI** and **MySQL** for managing student records and results with JWT authentication.

##  Tech Stack
- Python
- FastAPI
- MySQL
- SQLAlchemy
- JWT Authentication
- Pydantic

## Features
- User Registration & Login with JWT tokens
- Add, View, Update, Delete Students
- Add, View, Update, Delete Results
- Protected endpoints (authentication required)
- Auto-generated Swagger documentation

## Installation
```bash
# Clone the repository
git clone https://github.com/ishikathakare/student-result-api.git
cd student-result-api

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

##  Setup

Create a `.env` file in root directory:
```
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/student_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Create MySQL database:
```sql
CREATE DATABASE student_db;
```

##  Run the API
```bash
uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /auth/register | Register new user | No |
| POST | /auth/login | Login and get token | No |
| POST | /students/ | Add new student | Yes |
| GET | /students/ | Get all students | Yes |
| GET | /students/{id} | Get student by ID | Yes |
| PUT | /students/{id} | Update student | Yes |
| DELETE | /students/{id} | Delete student | Yes |
| POST | /results/ | Add result | Yes |
| GET | /results/{student_id} | Get student results | Yes |
| PUT | /results/{id} | Update result | Yes |
| DELETE | /results/{id} | Delete result | Yes |

## Author
Ishika Thakare
EOF
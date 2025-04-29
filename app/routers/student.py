from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.student import StudentOut
from app.schemas.grade import GradeOut

router = APIRouter(prefix="/student", tags=["student"])

@router.get("/profile", response_model=StudentOut)
def get_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return current_user.student

@router.get("/grades", response_model=list[GradeOut])
def get_grades(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return current_user.student.grades

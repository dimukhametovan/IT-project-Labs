from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_db, get_current_user
from app.models.user_m import User
from app.models.student_m import Student
from app.models.grade_m import Grade
from app.schemas.student import StudentOut
from app.schemas.grade import GradeOut

router = APIRouter(prefix="/student", tags=["student"])

@router.get("/profile", response_model=StudentOut)
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    student = db.query(Student).filter(Student.user_id == current_user.id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return student

@router.get("/grades", response_model=list[GradeOut])
def get_grades(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    student = db.query(Student).filter(Student.user_id == current_user.id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")

    grades = db.query(Grade).filter(Grade.student_id == student.id).all()
    return grades

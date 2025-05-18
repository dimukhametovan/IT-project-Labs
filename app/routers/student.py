from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.dependencies import get_db
# , get_current_user
from app.models.user_m import User
from app.models.student_m import Student
from app.models.grade_m import Grade
from app.schemas.student import StudentOut
from app.schemas.grade import GradeOut
from app.schemas.user import StudentProfileOut

router = APIRouter(prefix="/student", tags=["student"])

# @router.get("/profile", response_model=StudentOut)
# def get_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     return current_user.student

# @router.get("/grades", response_model=list[GradeOut])
# def get_grades(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     return current_user.student.grades

# @router.get("/profile", response_model=StudentProfileOut)
# def get_profile(
#     db: Session = Depends(get_db),
#     current_user=Depends(get_current_user)
# ):
#     student = db.query(Student).filter(Student.user_id == current_user.id).first()
#     if not student:
#         raise HTTPException(status_code=404, detail="Студент не найден")

#     return student


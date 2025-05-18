from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
# from app.auth.security import verify_password, create_access_token
from app.auth.dependencies import get_db
from app.models.user_m import User
from app.models.student_m import Student
from datetime import timedelta
from fastapi import Body
# from app.auth.security import get_password_hash
from app.schemas.user import UserRegister

router = APIRouter(prefix="/auth", tags=["auth"])
@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    if user.password != user.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )

    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    new_user = User(
        email=user.email,
        hashed_password=user.password,
        full_name=user.full_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    student_profile = Student(user_id=new_user.id)
    db.add(student_profile)
    db.commit()

    return {"message": "User successfully registered"}

# @router.post("/register")
# def register(
#     email: str = Body(...),
#     password: str = Body(...),
#     full_name: str = Body(...),
#     db: Session = Depends(get_db)
# ):
   
#     existing_user = db.query(User).filter(User.email == email).first()
#     if existing_user:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User with this email already exists"
#         )

    
#     new_user = User(
#         email=email,
#         hashed_password=get_password_hash(password),
#         full_name=full_name
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     student_profile = Student(user_id=new_user.id)
#     db.add(student_profile)
#     db.commit()

#     return {"message": "User successfully registered"}


# 

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # Находим пользователя по email
    user = db.query(User).filter(User.email == form_data.username).first()

    # Проверяем, что пользователь существует и пароль совпадает (без хеширования)
    if not user or form_data.password != user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    # Возвращаем просто подтверждение входа без токена
    return {
        "message": "Login successful",
        "user_id": user.id,
        "email": user.email,
        "full_name": user.full_name
    }
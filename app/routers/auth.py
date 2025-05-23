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

from datetime import timedelta
from fastapi import status
from app.auth.security import (
    create_access_token,
    verify_password,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

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
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or form_data.password != user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, 
        expires_delta=access_token_expires
    )

    return {
        "message": "Login successful",
        "user_id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "access_token": access_token,
        "token_type": "bearer"
    }
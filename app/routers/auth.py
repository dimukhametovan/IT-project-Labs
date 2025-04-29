from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.security import verify_password, create_access_token
from app.auth.dependencies import get_db
from app.models.user import User
from app.models.student import Student
from datetime import timedelta
from fastapi import Body
from app.auth.security import get_password_hash

router = APIRouter(prefix="/auth", tags=["auth"])

# @router.post("/login")
# def login(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: Session = Depends(get_db)
# ):
#     user = db.query(User).filter(User.email == form_data.username).first()
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password",
#         )

#     access_token_expires = timedelta(minutes=60)
#     access_token = create_access_token(
#         data={"sub": user.email},
#         expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
def register(
    email: str = Body(...),
    password: str = Body(...),
    full_name: str = Body(...),
    db: Session = Depends(get_db)
):
    # Проверка: пользователь с таким email уже есть
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    # Создание пользователя
    new_user = User(
        email=email,
        hashed_password=get_password_hash(password),
        full_name=full_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    student_profile = Student(user_id=new_user.id)
    db.add(student_profile)
    db.commit()

    return {"message": "User successfully registered"}

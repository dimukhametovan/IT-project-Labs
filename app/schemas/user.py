from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    full_name: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)
    confirm_password: str = Field(..., min_length=6)

# class UserRegister(BaseModel):
#     full_name: str
#     email: EmailStr
#     password: str
#     confirm_password: str


class StudentProfileOut(BaseModel):
    id: int
    full_name: str
    group: str
    study_form: str
    status: str
    email: str  

    class Config:
        from_attributes = True  

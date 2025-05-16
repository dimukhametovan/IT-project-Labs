from pydantic import BaseModel
from typing import Optional

class StudentProfileOut(BaseModel):
    id: int
    full_name: str
    group: str
    study_form: str
    status: str
    email: str  # из связанной модели User

    class Config:
        from_attributes = True  # для pydantic v2 (ранее было orm_mode = True)

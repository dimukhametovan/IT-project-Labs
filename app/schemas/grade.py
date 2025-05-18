from pydantic import BaseModel

class GradeOut(BaseModel):
    semester: int
    subject: str
    grade: int

    class Config:
        orm_mode = True

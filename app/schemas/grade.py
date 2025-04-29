from pydantic import BaseModel

class GradeOut(BaseModel):
    subject: str
    semester: str
    grade: str

    class Config:
        orm_mode = True

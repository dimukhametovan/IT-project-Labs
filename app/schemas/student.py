from pydantic import BaseModel

class StudentOut(BaseModel):
    full_name: str
    group: str
    education_form: str
    status: str

    class Config:
        orm_mode = True

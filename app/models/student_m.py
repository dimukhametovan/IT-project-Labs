from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    full_name = Column(String)
    group = Column(String)
    education_form = Column(String)  # очная/заочная
    status = Column(String)          # учится, отчислен и т.д.

    user = relationship("User", back_populates="student")
    grades = relationship("Grade", back_populates="student")
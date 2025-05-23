from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, student  
from fastapi.middleware.cors import CORSMiddleware
# from app.database import init_db
from app.models import grade_m, student_m, user_m

app = FastAPI()

# try:
#     Base.metadata.create_all(bind=engine)
#     print("Таблицы созданы успешно")
# except Exception as e:
#     print("Ошибка при создании таблиц:", e)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(student.router)




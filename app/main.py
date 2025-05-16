from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, student  # создашь позже
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# создаем таблиц
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # адрес твоего фронта
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# подключим маршруты позже
app.include_router(auth.router)
app.include_router(student.router)




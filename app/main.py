from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, student  # создашь позже

app = FastAPI()

# создаем таблиц
Base.metadata.create_all(bind=engine)

# подключим маршруты позже
app.include_router(auth.router)
app.include_router(student.router)

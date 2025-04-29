# Структура проекта (backend)

```pgsql
student_cabinet/
├── app/
│   ├── main.py              ← Точка входа: здесь запускается FastAPI и подключаются маршруты
│   ├── database.py          ← Подключение к SQLite и создание базовой схемы
│   ├── models/              ← SQLAlchemy модели — описывают таблицы БД
│   │   └── user.py          ← Модель пользователя (User)
│   ├── schemas/             ← Pydantic схемы — описывают входные/выходные данные API
│   │   └── user.py
│   ├── crud/                ← CRUD-функции (Create, Read, Update, Delete) — работа с БД
│   │   └── user.py
│   ├── auth/                ← Всё, что связано с авторизацией (JWT, хеширование пароля и т.п.)
│   │   ├── security.py      ← Хеширование паролей, создание токенов
│   │   └── dependencies.py  ← Получение текущего пользователя из токена
│   ├── routers/             ← Маршруты API (то, что отвечает на запросы)
│   │   └── auth.py
```

# Структура проекта (frontend)

```pgsql
frontend/
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── grades.html
│   └── ...
├── static/
│   ├── css/
│   └── js/

```

# Настрока среды окружения

```bash
# 1. Активируй виртуальное окружение

source venv/bin/activate      # на Linux/Mac
venv\Scripts\activate         # на Windows

# 2. Установи зависимости
pip install -r requirements.txt

# 3. Запусти сервер
uvicorn app.main:app --reload
```

Сервер: http://127.0.0.1:8000/docs

# Состав MVP-проекта "Личный кабинет студента"

- Регистрация и авторизация
- Просмотр профиля (по токену)
- Список предметов и оценок (успеваемость)

Этого достаточно, чтобы показать:

- защиту через JWT,
- работу с базой данных,
- модели данных и связи,
- базовую логику API.

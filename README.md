# 🛠 Технологии и библиотеки

Проект разработан с использованием следующих инструментов:

### 📦 Основные зависимости

| Библиотека  | Назначение                                  |
| ----------- | ------------------------------------------- |
| FastAPI     | Фреймворк для создания API (основа проекта) |
| SQLAlchemy  | ORM для работы с базой данных               |
| Pydantic    | Валидация данных и схемы API                |
| JWT         | Аутентификация и авторизация через токены   |
| Passlib     | Хеширование паролей (алгоритм bcrypt)       |
| Python-jose | Работа с JWT-токенами                       |

### 🗃 База данных

- SQLite (легковесная встроенная СУБД)

### ⚙️ Вспомогательные инструменты

- Uvicorn (ASGI-сервер для запуска FastAPI)
- Alembic (миграции БД, если используется)
- Pytest (тестирование, если есть тесты)

# Структура проекта

### Backend

```pgsql
it-project/
├── app/
│   ├── main.py              ← Точка входа: здесь запускается FastAPI и подключаются маршруты
│   ├── database.py          ← Подключение к SQLite и создание базовой схемы
│   ├── models/              ← SQLAlchemy модели — описывают таблицы БД
│   │   ├── grade_m.py       ← Модель оценок (Garde)
│   │   ├── student_m.py     ← Модель студента (Student)
│   │   └── user_m.py        ← Модель пользователя (User)
│   ├── schemas/             ← Pydantic схемы — описывают входные/выходные данные API
│   │   ├── grade.py
│   │   ├── student.py
│   │   └── user.py
│   ├── auth/                ← Всё, что связано с авторизацией (JWT, хеширование пароля и т.п.)
│   │   ├── security.py      ← Хеширование паролей, создание токенов
│   │   └── dependencies.py  ← Получение текущего пользователя из токена
│   ├── routers/             ← Маршруты API (регистрация, вход и профиль)
│   │   └── auth.py
│   │   └── student.py
```

### Frontend

```pgsql
student-cabinet/
├── public/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── grades.html
│   └── ...
├── src/
│   ├── api/
│   │   └── axios.js
│   ├── assets/
│   ├── pages/
│   │   ├── Login/
│   │   ├── Profile/
│   │   └── Register/
│   ├── App.jsx
│   └── index.js
├── package-lock.json
└── package.json

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

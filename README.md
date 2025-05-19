
# E-Store

A lightweight, high-performance e-commerce backend built with FastAPI. Manage products, categories, and reviews via a RESTful API with interactive docs.

---

## 🚀 Features

- CRUD operations for products and categories
- User reviews for products
- Automatic API docs (Swagger UI, ReDoc)
- Database migrations with Alembic
- Docker support for easy deployment

---

## 🛠 Tech Stack

- Python
- FastAPI
- SQLAlchemy + Alembic
- Uvicorn
- PostgreSQL
- Docker & Docker Compose

---

## 💾 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/Leifr22/e-store.git
   cd e-store
   ```
2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Setup & Run

1. Set the database URL (default: SQLite):

   ```bash
   export DATABASE_URL="sqlite:///./e_store.db"
   ```
2. Apply migrations:

   ```bash
   alembic upgrade head
   ```
3. Start the server:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
4. Open docs:

   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

---

## 📂 Project Structure

```
e-store/
├── migrations/                      # DB миграции
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── app/                          # Исходный код
│   ├── main.py                   # Точка входа в приложение
│   ├── backend/                  # Зависимости БД
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── db_depends.py
│   │
│   ├── models/                   # Pydantic / ORM модели
│   │   ├── categories.py
│   │   ├── products.py
│   │   ├── review.py
│   │   └── user.py
│   │
│   └── routers/                  # FastAPI маршруты
│       ├── __init__.py
│       ├── auth.py
│       ├── categories.py
│       ├── permission.py
│       └── products.py
│
├── docker-compose.yml           # Docker Compose
├── Dockerfile                   # Docker Image
├── requirements.txt             # Зависимости
├── alembic.ini                  # Настройка Alembic
├── README.md
└── .gitignore

```

---

## 🔜 Upcoming

- Extended admin rights function
- Shopping cart & orders
```

Этот README содержит всю необходимую информацию о проекте, включая особенности, используемые технологии, инструкции по установке и запуску, а также структуру проекта и планы на будущее. Если понадобится что-то дополнить или изменить, дайте знать!

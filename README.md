
# E-Store

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)](https://fastapi.tiangolo.com/)

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

- Python 3.7+
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
├── alembic/        # DB migrations
├── app/            # Source code
│   ├── main.py     # Entrypoint
│   ├── models.py   # ORM models
│   ├── schemas.py  # Pydantic schemas
│   ├── crud.py     # CRUD logic
│   └── routers/    # Routes (products, categories, reviews)
├── docker-compose.yml  # Docker Compose configuration
├── Dockerfile          # Docker image definition
├── requirements.txt
├── alembic.ini
├── README.md
└── .gitignore
```

---

## 🔜 Upcoming

- Extended admin rights function
- Shopping cart & orders
```

Этот README содержит всю необходимую информацию о проекте, включая особенности, используемые технологии, инструкции по установке и запуску, а также структуру проекта и планы на будущее. Если понадобится что-то дополнить или изменить, дайте знать!

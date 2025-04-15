# E-Store

This repository contains an e-store built with FastAPI, which allows users to manage products and categories.

## Description

The E-Store project is designed to demonstrate a simple yet functional e-commerce backend using FastAPI. It includes features such as:

- Product management: Create, read, update, and delete products.
- Category management: Organize products into categories for easier navigation.
- API documentation: Automatically generated and interactive API docs provided by FastAPI.
- Database migrations: Ensure your database schema is up-to-date by applying migrations.
- Logging: Application logs are generated for better monitoring and debugging.
- Celery with Redis: Asynchronous task processing using Celery and Redis.

## Features

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **CRUD operations**: Full support for creating, reading, updating, and deleting products and categories.
- **Product reviews**: Users can leave reviews for products to share their feedback.
- **Automatic API docs**: Interactive API documentation is automatically generated using Swagger UI and ReDoc.
- **Asynchronous processing**: Celery and Redis are used for background task execution.
- **Logging**: Integrated logging for monitoring application activity.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Leifr22/e-store.git
   ```

2. Navigate to the project directory:
   ```sh
   cd e-store
   ```

3. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

5. Apply migrations to set up the database schema:
   ```sh
   alembic upgrade head
   ```

6. Start Redis and Celery workers:
   ```sh
   redis-server
   celery -A app_name worker --loglevel=info
   ```

## Usage

1. Start the server:
   ```sh
   uvicorn main:app --reload
   ```

2. Access the API documentation at:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

3. Use the provided endpoints to manage products and categories.

## Project Structure

- `main.py`: The entry point of the application.
- `models.py`: Contains the database models.
- `schemas.py`: Defines the request and response schemas.
- `crud.py`: Implements the CRUD operations.
- `database.py`: Sets up the database connection.
- `endpoints/`: Contains the API route definitions.
- `tasks.py`: Defines Celery tasks.
- `logging_config.py`: Configures the logging.

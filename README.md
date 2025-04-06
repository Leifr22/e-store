# E-Store

This repository contains a small e-store built with FastAPI, which allows users to manage products and categories.

## Description

The E-Store project is designed to demonstrate a simple yet functional e-commerce backend using FastAPI. It includes features such as:

- Product management: Create, read, update, and delete products.
- Category management: Organize products into categories for easier navigation.
- API documentation: Automatically generated and interactive API docs provided by FastAPI.

## Features

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **CRUD operations**: Full support for creating, reading, updating, and deleting products and categories.
- **Automatic API docs**: Interactive API documentation is automatically generated using Swagger UI and ReDoc.

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
- Also review page is cooming soon

## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your proposed changes.

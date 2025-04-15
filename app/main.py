from fastapi import FastAPI, Request
from sqlalchemy.sql.ddl import CreateTable

from app.log import log_middleware
from app.models.categories import Category
from app.routers import categories, products, auth, permission,review
from app.tasks import background_task
app=FastAPI()
app.middleware('http')(log_middleware)
@app.get('/')
async def welcome():
    background_task.delay('Greetings')
    return {'message': 'Me e-commerce app'}
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(permission.router)
app.include_router(review.router)

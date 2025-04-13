from fastapi import FastAPI
from sqlalchemy.sql.ddl import CreateTable

from app.models.categories import Category
from app.routers import categories, products, auth, permission,review

app=FastAPI()
@app.get('/')
async def welcome():
    return {'message': 'Me e-commerce app'}
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(permission.router)
app.include_router(review.router)

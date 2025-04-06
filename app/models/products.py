from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.ddl import CreateTable

from app.backend.db import Base

class Product(Base):
    __tablename__='products'

    id=Column(Integer,primary_key=True, index=True)
    name=Column(String)
    slug=Column(String,unique=True, index=True)
    description=Column(String)
    price=Column(String)
    image_url=Column(String)
    stock=Column(Integer)
    rating=Column(Float)
    is_active=Column(Boolean,default=True)
    supplier_id=Column(Integer, ForeignKey('users.id'),nullable=True)
    category_id=Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')


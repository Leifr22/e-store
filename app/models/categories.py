from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Category(Base): #Cоздаем скелет таблицы
    __tablename__='categories'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    slug=Column(String, unique=True, index=True)
    products = relationship('Product', back_populates='category')

    is_active=Column(Boolean,default=True)


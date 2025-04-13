from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Category(Base): #Cоздаем скелет таблицы
    __tablename__='categories'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    slug=Column(String, unique=True, index=True)
    products = relationship('Product', back_populates='category')
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    is_active=Column(Boolean,default=True)
    parent = relationship("Category", remote_side=[id], backref="children")


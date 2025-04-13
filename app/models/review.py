from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.ddl import CreateTable

from app.backend.db import Base


class Review(Base):
    __tablename__='reviews'
    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey('users.id'))
    product_id=Column(Integer, ForeignKey('products.id'))
    comment=Column(Text,nullable=True)
    comment_date=Column(DateTime,server_default=func.now())
    grade=Column(Integer,nullable=True)
    is_active=Column(Boolean,default=True)

    user=relationship('User', back_populates='reviews')
    product=relationship('Product', back_populates='reviews')

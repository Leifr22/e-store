from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# Создаём базовый класс моделей СРАЗУ
class Base(DeclarativeBase):
    pass



# Создаём подключение к БД
DATABASE_URL = 'postgresql+asyncpg://postgres:postgres@db:5432/ecommerce' # Исправленный путь
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


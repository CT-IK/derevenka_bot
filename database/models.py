from sqlalchemy import Mapped, mapped_column, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base

from database.engine import Base


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False) # NULL
from sqlalchemy import Column, Integer, Text
from src.db.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(Integer, nullable=False, default=0)


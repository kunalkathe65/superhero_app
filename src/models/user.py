from sqlalchemy import Column, Integer, Text, Table, ForeignKey
from src.db.base import Base
from sqlalchemy.orm import relationship

favourite_superheroes = Table(
    "favourite_superheroes",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("superhero_id", Integer, ForeignKey("superheroes.superhero_id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(Integer, nullable=False, default=0)
    favourite_superheroes = relationship(
        "Superhero",
        secondary=favourite_superheroes,
        back_populates="favourite_by_user"
    )


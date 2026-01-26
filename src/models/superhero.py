from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import JSONB
from src.db.base import Base
from sqlalchemy.orm import relationship
from .team import member_superheroes
from .user import favourite_superheroes

class Superhero(Base):
    __tablename__ = "superheroes"

    superhero_id = Column(Integer, primary_key=True, index=True)
    name = Column(JSONB, nullable=False)
    powerstats = Column(JSONB, nullable=False)
    biography = Column(JSONB, nullable=False)
    appearance = Column(JSONB, nullable=False)
    work = Column(JSONB, nullable=False)
    connections = Column(JSONB, nullable=False)
    image_url = Column(JSONB, nullable=False)
    teams = relationship(
        "Team",
        secondary=member_superheroes,
        back_populates="member_superheroes"
    )
    favourite_by_user = relationship(
        "User",
        secondary=favourite_superheroes,
        back_populates="favourite_superheroes"
    )

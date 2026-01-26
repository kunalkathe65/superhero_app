from sqlalchemy import Column, Integer, Text, Table, ForeignKey
from src.db.base import Base
from sqlalchemy.orm import relationship

member_superheroes = Table(
    "member_superheroes",
    Base.metadata,
    Column("team_id", Integer, ForeignKey("teams.team_id"), primary_key=True),
    Column("superhero_id", Integer, ForeignKey("superheroes.superhero_id"), primary_key=True)
)

class Team(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    member_superheroes = relationship(
        "Superhero",
        secondary=member_superheroes,
        back_populates="teams"
    )
    intelligence = Column(Integer, nullable=False)
    strength = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    durability = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)
    combat = Column(Integer, nullable=False)


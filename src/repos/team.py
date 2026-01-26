from src.models.team import Team
from src.models.superhero import Superhero
from typing import List
from sqlalchemy.sql import func

class TeamRepository:

    def __init__(self,db):
        self.db=db

    def get_by_user_id(self, user_id) -> List[Team]:
        return self.db.query(Team).filter(Team.user_id == user_id).all()
    
    def get_by_name(self, name) -> Team:
        return self.db.query(Team).filter(Team.name == name).first()

    def create(self, data, user_id) -> Team:
        superheroes = (
            self.db.query(Superhero)
            .filter(Superhero.superhero_id.in_(data.member_superheroes))
            .all()
        )

        attrs = {
            "intelligence": 0,
            "strength": 0,
            "speed": 0,
            "durability": 0,
            "power": 0,
            "combat": 0,
        }

        for superhero in superheroes:
            stats = superhero.powerstats
            attrs["intelligence"] += int(stats["intelligence"])
            attrs["strength"] += int(stats["strength"])
            attrs["speed"] += int(stats["speed"])
            attrs["durability"] += int(stats["durability"])
            attrs["power"] += int(stats["power"])
            attrs["combat"] += int(stats["combat"])

        team = Team(
            name=data.name, 
            user_id=user_id,
            intelligence=attrs["intelligence"],
            strength=attrs["strength"],
            speed=attrs["speed"],
            durability=attrs["durability"],
            power=attrs["power"],
            combat=attrs["combat"],
            member_superheroes=superheroes,
            )
        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)
        return team
    
    def get_superheroes(self, limit) -> List[Superhero]:
        """
            Ideally to create teams we need to fetch limit * 6 records because each team will have 6 members.
            But we're fetching limit * 10 because records contains null as well and we must return 6 teams so this
            will give us some buffer.
        """
        superheroes = self.db.query(Superhero).limit(limit*10).all()
        if len(superheroes) % limit == 0:
            return superheroes
        return False
    
    def get_random_superheroes(self) -> Superhero:
        return self.db.query(Superhero).order_by(func.random()).limit(6).all()

    def get_all_teams(self) -> List[Team]:
        return self.db.query(Team).all()


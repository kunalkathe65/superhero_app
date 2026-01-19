from src.models.team import Team

class TeamRepository:

    def __init__(self,db):
        self.db=db

    def get_by_user_id(self, user_id):
        return self.db.query(Team).filter(Team.user_id == user_id).first()
    
    def get_by_name(self, name):
        return self.db.query(Team).filter(Team.name == name).first()

    def create(self, data) -> Team:
        team = Team(name=data.name, user_id=data.user_id)
        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)
        return team

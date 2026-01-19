from src.core.team_exceptions import TeamAlreadyExists, TeamNotFound

class TeamService:
    def __init__(self, repo):
        self.repo = repo

    def create_team(self, data):
        team_does_exist = self.repo.get_by_name(data.name)
        if team_does_exist:
            raise TeamAlreadyExists()
        return self.repo.create(data)
    
    def get_user_teams(self, data):
        teams = self.repo.get_by_user_id(data.user_id)
        if teams:
            return teams
        raise TeamNotFound
from src.core.user_exceptions import UserAlreadyExists, UserNotFound, InvalidPassword

class UserService:
    def __init__(self, repo):
        self.repo = repo

    def login_user(self, data):
        does_exist = self.repo.get_by_email(data.email)
        if not does_exist:
            raise UserNotFound()
        if does_exist.password_hash != data.password:
            raise InvalidPassword()
        return "token"

    
    def register_user(self, data):
        does_exist = self.repo.get_by_email(data.email)
        if does_exist:
            raise UserAlreadyExists()
        return self.repo.create(data)
    
    def create_team(self, data):
        return self.repo.create_team(data)
    
    def get_user_teams(self, data):
        return self.repo.get_user_teams(data)
    
    def assign_fav_superhero(self, data):
        return self.repo.assign_fav_superhero(data)
    
    def get_fav_superheroes(self, data):
        return self.repo.get_fav_superheroes(data)
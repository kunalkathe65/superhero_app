from src.core.user_exceptions import UserAlreadyExists, UserNotFound, InvalidPassword

class UserService:
    def __init__(self, repo):
        self.repo = repo

    def login_user(self, data):
        user_does_exist = self.repo.get_by_email(data.email)
        if not user_does_exist:
            raise UserNotFound()
        if user_does_exist.password_hash != data.password:
            raise InvalidPassword()
        return user_does_exist.user_id

    def register_user(self, data):
        user_does_exist = self.repo.get_by_email(data.email)
        if user_does_exist:
            raise UserAlreadyExists()
        return self.repo.create(data)
    
    def assign_fav_superhero(self, data):
        return self.repo.assign_fav_superhero(data)
    
    def get_fav_superheroes(self, data):
        return self.repo.get_fav_superheroes(data)
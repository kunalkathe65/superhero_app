from src.core.user_exceptions import UserAlreadyExists, NoFavSuperheroesFound, UserNotFound, InvalidPassword, SuperheroAlreadyFavourite

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
    
    def assign_fav_superhero(self, user_id, superhero_id):
        fav_assigned = self.repo.assign_fav_superhero(superhero_id, user_id)
        if fav_assigned:
            return fav_assigned
        raise SuperheroAlreadyFavourite()
    
    def get_fav_superheroes(self, user_id):
        fav_superheroes = self.repo.get_fav_superheroes_by_user_id(user_id)
        if fav_superheroes:
            return fav_superheroes
        raise NoFavSuperheroesFound()
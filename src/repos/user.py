from src.models.user import User
from src.models.superhero import Superhero

class UserRepository:

    def __init__(self,db):
        self.db=db

    def get_user_by_email(self, email) -> User:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, user_id) -> User:
        return self.db.query(User).filter(User.user_id == user_id).first()

    def create(self, data) -> User:
        user = User(email=data.email, password_hash=data.password, role=data.role)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def assign_fav_superhero(self, user_id: int, superhero_id: int):
        user = self.get_user_by_id(user_id)
        superhero = (
            self.db.query(Superhero)
            .filter(Superhero.superhero_id == superhero_id)
            .first()
        )
        if superhero not in user.favourite_superheroes:
            user.favourite_superheroes.append(superhero)
            self.db.commit()
            return True
        return False

    def get_fav_superheroes_by_user_id(self, user_id):
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user:
            return user.favourite_superheroes
        return False


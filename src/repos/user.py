from src.models.user import User

class UserRepository:

    def __init__(self,db):
        self.db=db

    def get_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()

    def create(self, data) -> User:
        user = User(email=data.email, password_hash=data.password, role=data.role)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

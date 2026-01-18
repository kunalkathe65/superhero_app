# app/dependencies/superhero.py
from fastapi import Depends
from src.services.user import UserService
from src.repos.user import UserRepository
from src.db.session import get_db

def get_user_repo(db=Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_user_service(
    repo: UserRepository = Depends(get_user_repo)
) -> UserService:
    return UserService(repo)

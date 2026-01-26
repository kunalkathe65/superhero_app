# app/dependencies/superhero.py
from fastapi import Depends
from src.services.superhero import SuperheroService
from src.repos.superhero import SuperheroRepository
from src.db.session import get_db

def get_superhero_repo(db=Depends(get_db)) -> SuperheroRepository:
    return SuperheroRepository(db)

def get_superhero_service(
    repo: SuperheroRepository = Depends(get_superhero_repo)
) -> SuperheroService:
    return SuperheroService(repo)

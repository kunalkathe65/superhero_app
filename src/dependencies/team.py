# app/dependencies/superhero.py
from fastapi import Depends
from src.services.team import TeamService
from src.repos.team import TeamRepository
from src.db.session import get_db

def get_team_repo(db=Depends(get_db)) -> TeamRepository:
    return TeamRepository(db)

def get_team_service(
    repo: TeamRepository = Depends(get_team_repo)
) -> TeamService:
    return TeamService(repo)

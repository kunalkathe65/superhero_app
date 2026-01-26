from fastapi import APIRouter, Depends, Header, HTTPException, status
from src.services.team import TeamService
from src.dependencies.team import get_team_service
from src.dependencies.verify_token import verify_token
from src.core.team_exceptions import BalancedTeamsNotFound, TeamNotFound, NotEnoughBalancedTeams, SpecialtyTeamsNotFound, NotEnoughSpecialtyTeams

router = APIRouter(prefix="/api/v1/team", tags=["teams"])

@router.get("/recommend/balanced")
def recommend_balanced_teams(
    limit: int = 6,
    service: TeamService = Depends(get_team_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        teams = service.recommend_balanced_teams(limit)
        if teams:
            return {"recommended_balanced_teams": teams}
    except BalancedTeamsNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No balanced team found"
        )
    except NotEnoughBalancedTeams:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough balanced teams found"
        )

@router.get("/recommend/specialty/{specialty_attribute}")
def recommend_specialty_team(
    specialty_attribute: str,
    limit: int = 6,
    service: TeamService = Depends(get_team_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        team = service.recommend_specialty_team(limit, specialty_attribute)
        if team:
            return {"recommended_specialty_team": team}
    except SpecialtyTeamsNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No specialty team found"
        )
    except NotEnoughSpecialtyTeams:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough specialty teams found"
        )

@router.get("/recommend/random")
def recommend_random_team(
    service: TeamService = Depends(get_team_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        team = service.recommend_random_team()
        if team:
            return {"random_team": team}
    except TeamNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )

@router.get("/list")
def list_all_teams(
    service: TeamService = Depends(get_team_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
):
    try:
        teams= service.list_all_teams()
        if teams:
            return {"teams_list": teams}
    except TeamNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teams not found"
        )
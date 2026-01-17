from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/team", tags=["teams"])

@router.get("/recommend/balanced")
def recommend_balanced_team(limit: int = 6):
    pass

@router.get("/recommend/specialty/{specialty_attribute}")
def recommend_specialty_team(limit: int = 6):
    pass

@router.get("/recommend/random")
def recommend_random_team():
    pass

@router.get("/list")
def list_all_teams():
    pass
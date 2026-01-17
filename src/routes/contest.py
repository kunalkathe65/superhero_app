from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/contest", tags=["contest"])

@router.get("/predict-winner/{team_id}/{opponent_team_id}")
def predict_winner():
    pass
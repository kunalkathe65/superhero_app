from fastapi import APIRouter
from src.schemas.superhero import UpdateSuperheroReq

router = APIRouter(prefix="/api/v1/superhero", tags=["superheroes"])

@router.get("/list")
def list_all_superheroes():
    pass

@router.get("/get/{superhero_id}")
def get_superhero_details():
    pass

@router.patch("/update/{superhero_id}")
def update_superhero_details(req: UpdateSuperheroReq):
    pass
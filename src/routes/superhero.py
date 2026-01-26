from fastapi import APIRouter
from src.schemas.superhero import UpdateSuperheroReq
from fastapi import APIRouter, Depends, status, HTTPException, Header
from src.services.superhero import SuperheroService
from src.dependencies.superhero import get_superhero_service
from src.dependencies.verify_token import verify_token
from src.core.superhero_exceptions import SuperheroNotFound
from src.core.user_exceptions import NotAuthorized

router = APIRouter(prefix="/api/v1/superhero", tags=["superheroes"])

@router.get("/list")
def list_all_superheroes(
    service: SuperheroService = Depends(get_superhero_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        superheroes = service.list_all_superheroes()
        if superheroes:
            return {"superheroes_list": superheroes}
    except SuperheroNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Superheroes not found"
        )

@router.get("/get/{superhero_id}")
def get_superhero_details(
    superhero_id: int,
    service: SuperheroService = Depends(get_superhero_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
):
    try:
        superhero = service.get_superhero_details(superhero_id)
        if superhero:
            return {"superhero_details": superhero}
    except SuperheroNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Superhero not found"
        )

@router.patch("/update/{superhero_id}")
def update_superhero_details(
    req: UpdateSuperheroReq,
    superhero_id: int,
    service: SuperheroService = Depends(get_superhero_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        updated_superhero = service.update_superhero_details(req, superhero_id, user)
        if updated_superhero:
            return {"messsage": "Details updated successfully"}
    except NotAuthorized:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update the details"
        )
    except SuperheroNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Superhero not found"
        )
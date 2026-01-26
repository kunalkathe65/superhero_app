from fastapi import APIRouter, Depends, Response, status, HTTPException, Header
from src.schemas.user import LoginReq, RegisterReq, CreateTeam
from src.services.user import UserService
from src.services.team import TeamService
from src.dependencies.user import get_user_service
from src.dependencies.team import get_team_service
from src.dependencies.verify_token import verify_token
from src.core.user_exceptions import UserNotFound, InvalidPassword, UserAlreadyExists, NoFavSuperheroesFound, SuperheroAlreadyFavourite
from src.core.team_exceptions import TeamAlreadyExists, TeamNotFound

router = APIRouter(prefix="/api/v1/user", tags=["users"])

@router.post("/login")
def login_user(
    req: LoginReq, 
    res: Response, 
    service: UserService = Depends(get_user_service)
    ):
    try:
        token = service.login_user(req)
        if token:
            res.set_cookie(
                key="token",
                value=token,
                httponly=True
            )
            return {"message": "Login successful"}
    except UserNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except InvalidPassword:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )

@router.post("/register")
def register_user(req: RegisterReq, service: UserService = Depends(get_user_service)):
    try:
        user = service.register_user(req)
        if user:
            return {"message": "Register successfully"}
    except UserAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

@router.post("/create-team")
def create_team(
    req: CreateTeam, 
    service: TeamService = Depends(get_team_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        team = service.create_team(req, user.user_id)
        if team:
            return {"message": "Team created successfully"}
    except TeamAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Team with same name already exists"
        )

@router.get("/get/teams")
def get_user_teams(
    service: TeamService = Depends(get_team_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        teams = service.get_user_teams(user.user_id)
        if teams:
            return {"teams": teams}
    except TeamNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="You have not formed any team"
        )

@router.post("/assign-fav/{superhero_id}")
def assign_fav_superhero(
    superhero_id: int,
    service: UserService = Depends(get_user_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        response = service.assign_fav_superhero(superhero_id, user.user_id)
        if response:
            return {"message": "Superhero successfully assigned as favourite"}
    except SuperheroAlreadyFavourite:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Superhero is already assigned as favourite"
        )

@router.get("/get/fav-superheroes")
def get_fav_superheroes(
    service: UserService = Depends(get_user_service),
    token: str = Header(..., description="Bearer token"),
    user = Depends(verify_token)
    ):
    try:
        fav_superheroes = service.get_fav_superheroes(user.user_id)
        if fav_superheroes:
            return {"fav_superheroes": fav_superheroes}
    except NoFavSuperheroesFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No favourite Superhero found"
        )
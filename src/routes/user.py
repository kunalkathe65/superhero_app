from fastapi import APIRouter, Depends, Response, status, HTTPException
from src.schemas.user import LoginReq, RegisterReq, CreateTeam
from src.services.user import UserService
from src.dependencies.user import get_user_service
from src.core.user_exceptions import UserNotFound, InvalidPassword, UserAlreadyExists

router = APIRouter(prefix="/api/v1/user", tags=["users"])

@router.post("/login")
def login_user(req: LoginReq, res: Response, service: UserService = Depends(get_user_service)):
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
def create_team(req: CreateTeam, service: UserService = Depends(get_user_service)):
    pass

@router.get("/get/teams")
def get_user_teams(service: UserService = Depends(get_user_service)):
    pass

@router.post("/assign-fav/{superhero_id}")
def assign_fav_superhero(service: UserService = Depends(get_user_service)):
    pass

@router.get("/get/fav-superheroes")
def get_fav_superheroes(service: UserService = Depends(get_user_service)):
    pass
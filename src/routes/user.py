from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/user", tags=["users"])

@router.post("/login")
def login_user():
    pass

@router.post("/register")
def register_user():
    pass

@router.post("/create-team")
def create_team():
    pass

@router.get("/get/teams")
def get_teams():
    pass

@router.post("/assign-fav/{superhero_id}")
def assign_fav_superhero():
    pass

@router.get("/get/fav-superheroes")
def get_fav_superheroes():
    pass
from fastapi import FastAPI
from src.routes.user import router as user_router
from src.routes.superhero import router as superhero_router
from src.routes.team import router as team_router
from src.routes.contest import router as contest_router

app = FastAPI()
app.include_router(user_router)
app.include_router(superhero_router)
app.include_router(team_router)
app.include_router(contest_router)
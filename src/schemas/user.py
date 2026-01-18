from pydantic import BaseModel, EmailStr
from typing import Optional

class LoginReq(BaseModel):
    email: EmailStr
    password: str

class RegisterReq(BaseModel):
    email: EmailStr
    password: str
    role: Optional[int] = 0

class CreateTeam(BaseModel):
    team_name: str
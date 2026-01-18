from fastapi import Request, HTTPException, status, Depends
from src.dependencies.user import get_user_repo
from src.repos.user import UserRepository

async def verify_token(
    request: Request,
    user_repo: UserRepository = Depends(get_user_repo),
):
    auth_header = request.headers.get("token")
    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing",
        )
    token = auth_header.replace("Bearer ", "")
    user = user_repo.get_user_by_id(int(token))
    if not user or token != str(user.user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token for this user",
        )
    return user

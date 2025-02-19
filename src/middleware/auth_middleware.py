from src.dependencies.get_token import decode_token
from fastapi import HTTPException
from fastapi import Request
from sqlalchemy.orm import Session
from fastapi import Depends
from src.dependencies.get_db import get_db
from src.dependencies.get_user import user_exist


async def get_current_user(request: Request, db: Session = Depends(get_db)):  # Ensure db session is passed here
    token = request.cookies.get("access_token")
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    payload = decode_token(token)  # Decode the token and extract the payload

    # Pass the db session to user_exist
    user = user_exist(payload['user_id'], db)  # Now db session is passed correctly
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return payload
from fastapi import HTTPException,Response
from fastapi.responses import JSONResponse
from src.models.user_model import UserModel
from src.models.auth_model import AuthModel
from src.dependencies.get_token import create_access_token

def login(req,db):
    user = db.query(UserModel).filter(UserModel.email == req.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    auth_user = db.query(AuthModel).filter(AuthModel.user_id == user.id).first()
    if not auth_user:
        raise HTTPException(status_code=404, detail="Authentication record not found")
    
    if not auth_user.verify_password(req.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    token = create_access_token({"user_id":auth_user.user_id,"name":user.name})
    response = JSONResponse(content={"message": "Login Successfully"})
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True,
        samesite="None",
        max_age=1800,
    )

    return response


def register(req,db):
    user = db.query(UserModel).filter(UserModel.email == req.email).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = UserModel(name=req.name,email=req.email)
    db.add(new_user)
    db.commit()
    
    new_auth = AuthModel(user_id=new_user.id,password=AuthModel.hash_password(req.password))
    db.add(new_auth)
    db.commit()
    
    return {"message":"User registered successfully"}


def logout():
    response = Response(content="Logout Successfully")
    response.delete_cookie("access_token")
    return response
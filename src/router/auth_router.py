from fastapi import APIRouter, Depends
from src.dependencies.get_db import get_db
from src.schemas.auth_schema import AuthLoginSchema, AuthRegisterSchema
from src.controller import auth_controller
router = APIRouter()

@router.post("/login")
def login_route(req:AuthLoginSchema, db=Depends(get_db)):
    return auth_controller.login(req,db)


@router.post("/register")
def register_route(req:AuthRegisterSchema, db=Depends(get_db)):
    return auth_controller.register(req,db)


@router.post("/logout")
def logout_route():
    return auth_controller.logout()
    
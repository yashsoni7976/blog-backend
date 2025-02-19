from fastapi import APIRouter,HTTPException,Depends
from src.dependencies.get_db import get_db
from src.controller import user_controller
from src.schemas.user_schema import UserCreateSchema, UserUpdateSchema


router = APIRouter()


@router.get("/")
def get_all_users_route(db=Depends(get_db)):
    return user_controller.get_all_users(db)


@router.get("/{user_id}")
def get_user_by_id_route(user_id: int, db=Depends(get_db)):
    return user_controller.get_user_by_id(db, user_id)


@router.post("/")
def create_user_route(req: UserCreateSchema, db=Depends(get_db)):
    if not req.name or not req.email or not req.phone:
        raise HTTPException(status_code=400, detail="Please provide all the details")
    return user_controller.create_user(db, req)


@router.put("/{user_id}")
def update_user_route(req: UserUpdateSchema, user_id: int, db=Depends(get_db)):
    return user_controller.update_user(db, user_id, req)


@router.delete("/{user_id}")
def delete_user_route(user_id: int, db=Depends(get_db)):
    return user_controller.delete_user(db, user_id)

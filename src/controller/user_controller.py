from fastapi import HTTPException
from src.models.user_model import UserModel


# Get ALl the Users
def get_all_users(db):
    user = db.query(UserModel).all()
    if not user:
        raise HTTPException(status_code=404, detail="No users found")
    return HTTPException(status_code=200, detail=user)


# Get User by ID
def get_user_by_id(db,user_id):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return HTTPException(status_code=200, detail=user)


# Create a new User
def create_user(db,req):
    user = db.query(UserModel).filter(UserModel.email == req.email).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = UserModel(name=req.name,email=req.email,phone=req.phone)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return HTTPException(status_code=201, detail=new_user)


# Delete a User
def delete_user(db,user_id):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return HTTPException(status_code=200, detail="User deleted successfully")


# Update a User
def update_user(db,user_id,req):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = req.name
    user.email = req.email
    user.phone = req.phone
    user.is_active = req.is_active
    db.commit()
    db.refresh(user)
    return HTTPException(status_code=200, detail=user)
from sqlalchemy.orm import Session
from src.models.user_model import UserModel

def user_exist(user_id: int, db: Session):  # Expect the db session directly here
    # Query the database for the user by user_id
    return db.query(UserModel).filter(UserModel.id == user_id).first()
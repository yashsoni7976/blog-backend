from src.database.db_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthModel(Base):
    __tablename__ = "Auth_Table"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey("User_Table.id"), nullable=False)
    password = Column(String)

    user = relationship("UserModel", back_populates="auth")

    def hash_password(password):
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)

        
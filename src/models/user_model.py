from src.database.db_config import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, func
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = 'User_Table'

    id= Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(10))
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.timezone("Asia/Calcutta", func.now()))

    auth = relationship("AuthModel", back_populates="user", uselist=False)
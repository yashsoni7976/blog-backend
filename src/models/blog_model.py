from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database.db_config import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, TIMESTAMP


class BlogModel(Base):
    __tablename__ = "Blog_Table"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.timezone("Asia/Calcutta", func.now()))
    is_active = Column(Boolean, nullable=False, default=True)

    user_id = Column(Integer, ForeignKey("User_Table.id"), nullable=False)

    user = relationship("UserModel", back_populates="blogs")


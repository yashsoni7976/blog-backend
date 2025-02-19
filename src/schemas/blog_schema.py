from pydantic import BaseModel

class BlogSchema(BaseModel):
    title: str
    content: str
    is_active: bool
    user_id: int

    class Config:
        from_attributes = True

class BlogCreateSchema(BaseModel):
    title: str
    content: str
    user_id: int

    class Config:
        from_attributes = True


class BlogUpdateSchema(BaseModel):
    title: str
    content: str
    is_active: bool
    class Config:
        from_attributes = True
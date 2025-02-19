from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    is_active: bool
    created_at: str

    class Config:
        from_attributes = True

class UserCreateSchema(BaseModel):
    name: str
    email: str
    phone: str

    class Config:
        from_attributes = True

class UserUpdateSchema(BaseModel):
    name: str
    email: str
    phone: str
    is_active: bool

    class Config:
        from_attributes = True
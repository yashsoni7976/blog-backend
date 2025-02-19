from pydantic import BaseModel

class AuthLoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True



class AuthRegisterSchema(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



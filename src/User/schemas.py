from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    password: str
    name: str
    email: str

class SelectUserSchema(BaseModel):
    id: int
    name: str

class AuthUserSchema(BaseModel):
    password:str
    email:str

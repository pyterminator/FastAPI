from pydantic import BaseModel


class ValidateUser(BaseModel):
    username: str 
    email: str 
    password: str 


class ValidateLogin(BaseModel):
    email: str 
    password: str 
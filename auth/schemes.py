from pydantic import BaseModel, field_validator, EmailStr
from utils.check_password import PasswordChecker
from fastapi import HTTPException, status
from string import ascii_lowercase

class ValidateUser(BaseModel):
    username: str 
    email: EmailStr
    password: str 

    @field_validator("password")
    def check_password(cls, password):
        if not PasswordChecker.check_password(password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Şifrə minimum 8 simvoldan ibarət olmalıdır. Tərkibində ən az bir böyük hərf, 1 kiçik hərf, 1 rəqəm və nöqtə olmalıdır")
        return password
    
    @field_validator("username")
    def check_username(cls, username):
        for ch in username:
            if ch not in ascii_lowercase:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="İstifadəçi adında yalnız 26 kiçik ingilis hərfi olmalıdır!")
        return username

class ValidateLogin(BaseModel):
    email: str 
    password: str 
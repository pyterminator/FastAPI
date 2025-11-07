from fastapi import APIRouter
from auth.schemes import ValidateUser, ValidateLogin
from auth.models import User
from utils.hashing import Hash

router = APIRouter()


@router.post('/create/')
async def create_new_user(data: ValidateUser):
    new_user = User(email=data.email, username=data.username)
    new_user.set_password(data.password)
    await new_user.save()
    return new_user

@router.post('/login/')
async def login_user(data: ValidateLogin):
    
    if user := await User.get_or_none(email=data.email):
        verify = Hash.verify(data.password, user.password)
        return verify

    return {"error": "False"}
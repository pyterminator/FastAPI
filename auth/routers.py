from auth.models import User
from utils.hashing import Hash
from tortoise.expressions import Q
from utils.check_password import PasswordChecker
from fastapi import APIRouter, HTTPException, status
from auth.schemes import ValidateUser, ValidateLogin
from utils.token_manager import TokenManager

router = APIRouter()


@router.post('/sign-up')
async def sign_up(data: ValidateUser):
    get_user = await User.get_or_none(Q(email=data.email) | Q(username=data.username))
    if get_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username və ya Email artıq istifadə olunmuşdur")
    else:
        new_user = User(email=data.email, username=data.username)
        new_user.set_password(data.password)
        await new_user.save()
        return new_user

@router.post('/sign-in')
async def sign_in(data: ValidateLogin):
    
    if user := await User.get_or_none(email=data.email):
        verify = Hash.verify(data.password, user.password)
        if verify:
            access_token = TokenManager.create_jwt({"id":user.id})
            return {
                "token": access_token,
                "type": "bearer"
            }
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="İstifadəçi məlumatları doğru deyil")

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="İstifadəçi tapılmadı")
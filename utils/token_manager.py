import os 
from jose import jwt 
from auth.models import User
from dotenv import load_dotenv
from datetime import timedelta, datetime, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
EXPIRE_DATE = int(os.getenv("EXPIRE_DATE"))
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY_FOR_REFRESH_TOKEN = os.getenv("SECRET_KEY_FOR_REFRESH_TOKEN", SECRET_KEY)
EXPIRE_DATE_FOR_REFRESH_TOKEN = int(os.getenv("EXPIRE_DATE_FOR_REFRESH_TOKEN", EXPIRE_DATE))


bearer_scheme = HTTPBearer()

class TokenManager:

    @staticmethod
    def create_jwt(data: dict):
        to_encode = data.copy()
        expire_date = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_DATE)
        to_encode.update({"exp": int(expire_date.timestamp())})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def create_refresh_token(data: dict):
        to_encode = data.copy()
        expire_date = datetime.now(timezone.utc) + timedelta(days=EXPIRE_DATE_FOR_REFRESH_TOKEN)
        to_encode.update({"exp": int(expire_date.timestamp())})
        return jwt.encode(to_encode, SECRET_KEY_FOR_REFRESH_TOKEN, algorithm=ALGORITHM)

    @staticmethod
    async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
        token = credentials.credentials
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: int = payload.get("id")
            if user_id:
                user = await User.get_or_none(id=user_id)
                if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="İstifadəçi tapılmadı!")
                return user
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token-də problem oldu")
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token verify hissəsində problem oldu")

    @staticmethod
    def verify_refresh_token(refresh_token: str):
        try:
            payload = jwt.decode(refresh_token, SECRET_KEY_FOR_REFRESH_TOKEN, algorithms=[ALGORITHM])
            user_id: int = payload.get("id")
            if user_id: return user_id 
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token-də problem oldu")
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token verify hissəsində problem oldu")

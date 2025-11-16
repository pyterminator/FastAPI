import os 
from jose import jwt 
from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
EXPIRE_DATE = int(os.getenv("EXPIRE_DATE"))
ALGORITHM = os.getenv("ALGORITHM")


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in')
bearer_scheme = HTTPBearer()

class TokenManager:

    @staticmethod
    def create_jwt(data: dict):
        to_encode = data.copy()
        expire_date = datetime.now() + timedelta(minutes=EXPIRE_DATE)
        to_encode.update({"exp": expire_date})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    

    @staticmethod
    def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
        token = credentials.credentials
        # def get_current_user(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: int = payload.get("id")
            if user_id: return user_id 
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token-də problem oldu")
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token verify hissəsində problem oldu")
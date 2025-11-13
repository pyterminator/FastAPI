import os 
from jose import jwt 
from dotenv import load_dotenv
from datetime import timedelta, datetime

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
EXPIRE_DATE = int(os.getenv("EXPIRE_DATE"))
ALGORITHM = os.getenv("ALGORITHM")


class TokenManager:

    @staticmethod
    def create_jwt(data: dict):
        to_encode = data.copy()
        expire_date = datetime.now() + timedelta(minutes=EXPIRE_DATE)
        to_encode.update({"exp": expire_date})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
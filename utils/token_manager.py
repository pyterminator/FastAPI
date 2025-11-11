from datetime import timedelta, datetime
from jose import jwt 

SECRET_KEY = "mushvigshukurov2002mushvigshukurov2002"
ALGORITHM = "HS256"
EXPIRE_DATE = 5

class TokenManager:

    @staticmethod
    def create_jwt(data: dict, expire_date: timedelta|None = None):
        to_encode = data.copy()

        if expire_date:
            expire_date = datetime.now() + expire_date
        else:
            expire_date = datetime.now() + timedelta(minutes=EXPIRE_DATE)
        
        to_encode.update({"exp": expire_date})

        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


data = {"id": 5, "mode": "read"}
expire_date = timedelta(minutes=15)

my_jwt_token = TokenManager.create_jwt(data, expire_date)
print(my_jwt_token)
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


class Hash:

    @staticmethod
    def encrypt(raw_password: str):
        return pwd_context.hash(raw_password)


    @staticmethod
    def verify(raw_password: str, hash_password: str):
        return pwd_context.verify(raw_password, hash_password)
    
    
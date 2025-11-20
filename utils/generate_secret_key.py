import secrets 
SECRET_KEY = secrets.token_hex(32)
if __name__ == "__main__": print(SECRET_KEY)
import re 

class EmailChecker:

    @staticmethod 
    def check_email(email:str)->bool:
        pattern = r"^[A-Za-z0-9](?:[A-Za-z0-9._-]{1,}[A-Za-z0-9])?@[A-Za-z0-9](?:[A-Za-z0-9-]{0,}[A-Za-z0-9])?(?:\.[A-Za-z]{2,})+$"
        if re.match(pattern, email) and isinstance(email, str): return True 
        return False 

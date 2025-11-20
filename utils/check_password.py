import re

class PasswordChecker:
    @staticmethod
    def check_password(password: str)->bool:
        pattern = r"^(?=.*[A-ZÜŞÇİĞÖƏ])(?=.*[a-züçşıəöğ])(?=.*\d)(?=.*\.)[A-Za-z0-9.üçşıəöğÜŞÇİĞÖƏ]{8,}$"
        if isinstance(password, str):
            if re.match(pattern, password): return True
            else: return False
        return False
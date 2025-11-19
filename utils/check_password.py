


class PasswordChecker:

    @staticmethod
    def check_password(password: str)->bool:
        has_upper, has_lower, has_digit = (False, False, False)

        for ch in password:
            if ch.isupper(): has_upper = True
            elif ch.islower(): has_lower = True
            elif ch.isdigit(): has_digit = True

        if not all([has_upper, has_lower, has_digit]):
            return False 

        if len(password) < 8:
            return False

        return True

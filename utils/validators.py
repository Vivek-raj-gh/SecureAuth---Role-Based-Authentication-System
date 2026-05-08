from email_validator import validate_email, EmailNotValidError
import re

def validate_user_email(email):

    try:
        validate_email(email)
        return True

    except EmailNotValidError:
        return False

def validate_password(password):

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    return True
import re


def validate_name(name):

    if len(name.strip()) < 3:
        return False

    if not name.replace(" ", "").isalpha():
        return False

    return True


def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(pattern, email)


def validate_phone(phone):

    if not phone.isdigit():
        return False

    if len(phone) != 10:
        return False

    return True
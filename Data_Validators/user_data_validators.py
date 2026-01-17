import re

def validate_id_number(id_number: str) -> bool:
    return bool(re.fullmatch(r"\d{14}", id_number))

def validate_name(name: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z ]{2,}", name.strip()))

def validate_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))

def validate_egyptian_mobile(mobile: str) -> bool:
    return bool(re.fullmatch(r"01[0-2,5]\d{8}", mobile))
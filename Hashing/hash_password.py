def hash_password(password: str):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()
import hashlib

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def verify_token(token: str, stored: str) -> bool:
    return hashlib.sha1(token.encode()).hexdigest() == stored

def generate_checksum(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()
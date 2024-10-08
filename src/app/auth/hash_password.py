from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_hash(password: str):
    """Хеширование пароля"""
    return pwd_context.hash(password)


def verify_hash(plain_password: str, hashed_password: str):
    """Верифицация пароля"""
    return pwd_context.verify(plain_password, hashed_password)

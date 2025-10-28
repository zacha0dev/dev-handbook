from hashlib import sha256
import bcrypt
from ..core.settings import settings

def _mix_bytes(plain: str) -> bytes:
    """
    Pre-hash with SHA-256 + server-side pepper.
    Returns 32 bytes (digest), safely under bcrypt's 72-byte limit.
    """
    return sha256((plain + settings.pepper).encode("utf-8")).digest()

def hash_password(plain: str) -> str:
    salt = bcrypt.gensalt(rounds=settings.bcrypt_rounds)  # int rounds from env
    hashed = bcrypt.hashpw(_mix_bytes(plain), salt)
    return hashed.decode("utf-8")  # store as str

def verify_password(plain: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(_mix_bytes(plain), hashed.encode("utf-8"))
    except Exception:
        return False

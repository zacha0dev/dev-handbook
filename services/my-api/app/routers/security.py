from fastapi import APIRouter, Query
from ..services.security_service import hash_password, verify_password
from ..schemas.security import HashResponse

router = APIRouter(prefix="/security", tags=["security"])

@router.get("/hash", response_model=HashResponse)
def hash_endpoint(password: str = Query(..., min_length=3, description="Plaintext to hash")):
    hashed = hash_password(password)
    return HashResponse(bcrypt_hash=hashed, verified_roundtrip=verify_password(password, hashed))

@router.get("/verify")
def verify_endpoint(password: str = Query(..., min_length=3), hash: str = Query(...)):
    return {"ok": verify_password(password, hash)}

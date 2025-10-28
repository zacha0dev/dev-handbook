from pydantic import BaseModel, Field

class HashResponse(BaseModel):
    bcrypt_hash: str
    verified_roundtrip: bool

class VerifyQuery(BaseModel):
    password: str = Field(..., min_length=3)
    hash: str

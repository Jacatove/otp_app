from pydantic import BaseModel
from uuid import UUID

class RegisterRequest(BaseModel):
    user_id: UUID

class RegisterResponse(BaseModel):
    otpauth_url: str

class ValidateRequest(RegisterRequest):
    code: str  # ← ahora string

class ValidateResponse(BaseModel):
    valid: bool
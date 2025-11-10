from pydantic import BaseModel, UUID4


class RegisterRequest(BaseModel):
    user_id: UUID4

class RegisterResponse(BaseModel):
    otpauth_url: str

class ValidateRequest(RegisterRequest):
    code: int

class ValidateResponse(BaseModel):
    valid: bool

from fastapi import HTTPException, status, Security
from fastapi.security import APIKeyHeader

from config import settings


header_scheme = APIKeyHeader(name="x-key")

def check_api_key(
    header_key: str = Security(header_scheme),
):
    if not header_key == settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )

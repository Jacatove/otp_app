from fastapi import FastAPI, HTTPException, Depends, status, Security


from otp_service import OtpService
from scheme import ValidateRequest, ValidateResponse, RegisterResponse, RegisterRequest

from database import SessionDep
from authentication import check_api_key

app = FastAPI(title="OTP Service")


@app.get("/key/", dependencies=[Security(check_api_key)])
async def read_items():
    return True


def get_service(db_session: SessionDep) -> OtpService:
    return OtpService(db_session)


@app.post(
        "/otp/register",
        response_model=RegisterResponse,
        dependencies=[Security(check_api_key)],
)
def register(req: RegisterRequest, svc: OtpService = Depends(get_service)):
    url = svc.register_user(str(req.user_id))
    return RegisterResponse(otpauth_url=url)


@app.post(
        "/otp/validate",
        response_model=ValidateResponse,
        dependencies=[Security(check_api_key)],
)

@app.post(
    "/otp/validate",
    response_model=ValidateResponse,
    dependencies=[Security(check_api_key)],
)
def validate(req: ValidateRequest, svc: OtpService = Depends(get_service)):
    is_otp_valid = svc.validate_otp(
        str(req.user_id),     # aseguramos string
        req.code,
    )

    if not is_otp_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Código inválido o ya utilizado recientemente.",
        )

    return ValidateResponse(valid=True)

import pyotp
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import User2FA


class OtpService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_id: str) -> str:
        """
        Genera un secreto nuevo para el usuario y lo guarda en DB.
        Devuelve la URL otpauth para generar el QR.
        Si el usuario ya tiene secreto, lo regenera (útil para "perdí el celular").
        """
        secret = pyotp.random_base32()  # 16 caracteres, estándar
        totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(
            name=user_id,
            issuer_name="CiberProyecto"  # Cambia por el nombre de tu app/proyecto
        )

        # Upsert: si existe, actualiza el secreto
        user_2fa = User2FA(user_id=user_id, secret=secret, last_auth_at=None)
        self.db.merge(user_2fa)  # merge hace upsert
        self.db.commit()

        return totp_uri  # Ej: otpauth://totp/CiberProyecto:123e4567-e89b-12d3-a456-426614174000?secret=NBW7Z3T5KX123456&issuer=CiberProyecto

    def validate_otp(self, user_id: str, code: str) -> bool:
        user: User2FA = self.db.query(User2FA).filter(User2FA.user_id == user_id).first()
        if not user:
            return False

        totp = pyotp.TOTP(user.secret)
        
        # Acepta el código como string y quita espacios
        if not totp.verify(code.strip(), valid_window=30):
            return False

        now = datetime.utcnow()
        if user.last_auth_at and (now - user.last_auth_at) < timedelta(seconds=30):
            return False

        user.last_auth_at = now
        self.db.commit()
        return True
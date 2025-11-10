from pydantic import UUID4
from sqlalchemy.orm.session import Session


class OtpService:

    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_id: str) -> str:
        """Recibir petición del API y regresar"""
        print('Registrando.')
        print('user_id', user_id)
        return 'url-propuesta'

    def validate_otp(self, user_id: UUID4, code: int) -> bool:
        """"""
        print('validar código otp de user_id, como es el proceso inicial?')
        return True

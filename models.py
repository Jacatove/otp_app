# models.py
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User2FA(Base):
    __tablename__ = "users_2fa"

    user_id = Column(String(36), primary_key=True)
    secret = Column(String(32), nullable=False)
    last_auth_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
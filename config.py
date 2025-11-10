"""Configuration Module."""
from pydantic import MySQLDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """App configuration class."""

    # API KEY Authentication
    API_KEY: str

    # DataBase
    MYSQL_SERVER: str
    MYSQL_PORT: int = 3306
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(  # pylint: disable=invalid-name
        self,
    ) -> MySQLDsn:
        """Database URI for SQLAlchemy using MySQL."""
        return MultiHostUrl.build(
            scheme="mysql+mysqlconnector",
            username=self.MYSQL_USER,
            password=self.MYSQL_PASSWORD,
            host=self.MYSQL_SERVER,
            port=self.MYSQL_PORT,
            path=self.MYSQL_DB,
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
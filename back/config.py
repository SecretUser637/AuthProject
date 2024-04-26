from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sql_app.sqlite"

    EMAIL_SMTP:str
    EMAIL_PORT:str='465'
    EMAIL_LOG:str
    EMAIL_PWD:str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
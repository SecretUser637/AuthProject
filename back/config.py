from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sql_app.sqlite"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
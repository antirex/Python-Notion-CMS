from pydantic import BaseSettings
from dotenv import dotenv_values

config = dotenv_values(".env")


class CommonSettings(BaseSettings):
    APP_NAME: str = "Notion CMS"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000


class NotionSettings(BaseSettings):
    TOKEN: str = config["token"]
    THOUGHT_EXPERIMENTS_DATABASE_ID: str = config["thought_experiments_database_id"]
    EXPERIENCE_DESIGN_DATABASE_ID: str = config["experience_design_database_id"]


class Settings(CommonSettings, ServerSettings, NotionSettings):
    pass


settings = Settings()

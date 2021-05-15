from pydantic import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str
    STATIC_FILES_ROOT: str

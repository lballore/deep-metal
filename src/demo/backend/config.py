from pydantic import BaseSettings

class Settings(BaseSettings):
    STATIC_FILES_ROOT: str

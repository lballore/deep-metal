from enum import Enum

from pydantic import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str
    STATIC_FILES_ROOT: str


class HyperParameters(object):
    BOS_TOKEN_ID=50257
    DO_SAMPLE=True
    EOS_TOKEN_ID=50256
    NUM_RETURN_SEQUENCES=1
    TOP_K=0
    TOP_P=0.97
    USE_CACHE=True

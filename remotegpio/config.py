"""
Stores configuration options passed as environment variables.
"""
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    build_time: str = 'unknown'
    short_sha: str = 'manual'
    max_press_delay: int = 60*60*1000


@lru_cache
def get_settings():
    return Settings()

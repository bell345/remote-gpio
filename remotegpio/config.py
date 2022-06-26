"""
Stores configuration options passed as environment variables.
"""
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    aws_region: str = 'us-east-1'
    build_time: str = 'unknown'
    short_sha: str = 'manual'
    media_bucket_name: str = 'media-bucket'
    media_max_file_size: int = 50 * 1024 * 1024
    media_user_quota: int = 1000
    frontend_canonical_id: str = ''


@lru_cache
def get_settings():
    return Settings()

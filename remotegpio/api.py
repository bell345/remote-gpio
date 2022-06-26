"""All of the endpoints are defined in this file."""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .config import Settings, get_settings

api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:4200'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@api.get('')
@api.get('/')
@api.get('/version')
async def hello(settings: Settings = Depends(get_settings)):
    return {
        'build_time': settings.build_time,
        'commit': settings.short_sha
    }

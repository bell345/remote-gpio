"""All of the endpoints are defined in this file."""

from asyncio import sleep

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from RPi import GPIO
GPIO.setmode(GPIO.BCM)

from . import exceptions
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


@api.put('/gpio/{port}/on')
async def turn_on(port: int):
    if port < 0 or port > 53:
        return exceptions.BadRequest.response(f'GPIO{port} is not a valid port')

    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, GPIO.HIGH)

    return ''

@api.put('/gpio/{port}/off')
async def turn_off(port: int):
    if port < 0 or port > 53:
        return exceptions.BadRequest.response(f'GPIO{port} is not a valid port')

    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, GPIO.LOW)

    return ''

@api.put('/gpio/{port}/press')
async def press(port: int,
                delay_ms: int = 200,
                settings: Settings = Depends(get_settings)):
    if port < 0 or port > 53:
        return exceptions.BadRequest.response(f'GPIO{port} is not a valid port')

    if delay_ms < 0 or delay_ms > settings.max_press_delay:
        return exceptions.BadRequest.response(
            f'Press delay of {delay_ms} ms is over the limit of '+
            f'{settings.max_press_delay} ms')

    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, GPIO.HIGH)
    await sleep(delay_ms / 1000)
    GPIO.output(port, GPIO.LOW)

    return ''

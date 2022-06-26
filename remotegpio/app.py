"""
This file is used for initial setup when the Lambda function instance is spun
up, and sets up general paths for the API routes as well.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .api import api


def create_app():
    app = FastAPI()
    app.mount('/api', api)
    app.mount('/', StaticFiles(directory='static', html=True), name='static')
    return app


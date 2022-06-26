from fastapi.testclient import TestClient

import pytest

from remotegpio.app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return TestClient(app)


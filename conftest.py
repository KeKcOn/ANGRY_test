import pytest

from app import create_app

@pytest.fixture
def cli(event_loop, aiohttp_client):
    app = create_app()
    return event_loop.run_until_complete(aiohttp_client(app))
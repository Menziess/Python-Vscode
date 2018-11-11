from src.app import app
import pytest


@pytest.fixture
def client():
    client = app.test_client()

    # Before

    yield client

    # After


def test_hello_route(client):
    r = client.get('/')
    assert b'Hello ' in r.data


def test_fib_route(client):
    r = client.get('/fib/4')
    assert b'Fibonacci of 4 is 5' in r.data

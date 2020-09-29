from app import fibapp
import pytest

@pytest.fixture
def client():
    return fibapp.test_client()

def test_string(client):
    response = client.get('/fib/hehe')
    assert response.status_code == 404

def test_smaller_num(client):
    response = client.get('/fib/1')
    assert response.status_code == 404


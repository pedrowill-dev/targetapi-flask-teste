import pytest
import json
from src import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_should_return_status_code_200(client):
    username = 'soniblane'
    password = 'blanesoni'

    login_data = {'username': username, 'password': password}
    response = client.post('/auth/login', json=login_data)

    assert response.status_code == 200
    assert 'token' in json.loads(response.data)


def test_password_should_return_status_code_401_not_exist(client):
    username = 'soniblane'
    password = 'blanesonsddi'

    login_data = {'username': username, 'password': password}
    response = client.post('/auth/login', json=login_data)

    assert response.status_code == 401
    assert 'Senha incorreta' == json.loads(response.data)['message']


def test_username_should_return_status_code_401_not_exist(client):
    username = 'sonsssdasdia'
    password = 'sonia123'

    login_data = {'username': username, 'password': password}
    response = client.post('/auth/login', json=login_data)

    assert response.status_code == 401
    assert 'Usuario não existe' == json.loads(response.data)['message']



def test_key_error_should_return_status_code_401(client):
    username = 'sonia'
    password = 'sonia123'

    login_data = {'usernsame': username, 'password': password}
    response = client.post('/auth/login', json=login_data)

    assert response.status_code == 400
    assert 'token' not in json.loads(response.data)


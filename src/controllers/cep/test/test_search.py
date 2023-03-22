
import pytest
from src import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_search_should_return_cep_valid():
    with app.test_client() as client:
        # Authenticate with username and password
        username = 'sonia'
        password = 'sonia123'
        login_data = {'username': username, 'password': password}
        response = client.post('/auth/login', json=login_data)
        token = json.loads(response.data)['token']

        # Make API call with the client and pass the token in headers
        data = {'cep': '03289020'}
        headers = {'x-access-token': token}
        response = client.post('/cep/search', data=json.dumps(data), content_type='application/json', headers=headers)

        assert response.status_code == 200
        assert 'cidade' and 'info_cep' in json.loads(response.data)


def test_search_should_return_cep_invalid():
    with app.test_client() as client:
        # Authenticate with username and password
        username = 'sonia'
        password = 'sonia123'
        login_data = {'username': username, 'password': password}
        response = client.post('/auth/login', json=login_data)
        token = json.loads(response.data)['token']

        # Make API call with the client and pass the token in headers
        data = {'cep': '03289021sds'}
        headers = {'x-access-token': token}
        response = client.post('/cep/search', data=json.dumps(data), content_type='application/json', headers=headers)

        assert response.status_code == 400
        assert 'inválido' in json.loads(response.data)['message']


def test_search_should_return_city_not_found():
    with app.test_client() as client:
        # Authenticate with username and password
        username = 'sonia'
        password = 'sonia123'
        login_data = {'username': username, 'password': password}
        response = client.post('/auth/login', json=login_data)
        token = json.loads(response.data)['token']

        # Make API call with the client and pass the token in headers
        data = {'cep': '03289021'}
        headers = {'x-access-token': token}
        response = client.post('/cep/search', data=json.dumps(data), content_type='application/json', headers=headers)

        assert response.status_code == 404
        assert 'CEP não encontrado' in json.loads(response.data)['message']

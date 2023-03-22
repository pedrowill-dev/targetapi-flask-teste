import pytest
import json
from src import app, mongo
from werkzeug.security import check_password_hash



@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register_user_should_status_code_201(client):
    # Teste de registro de usuário válido
    username = 'usedsdsr1'
    password = '123456'
    user_data = {'username': username, 'password': password}
    response = client.post('/auth/signup', json=user_data)

    assert response.status_code == 201
    assert 'id' in json.loads(response.data)

    # Verifica se o usuário foi adicionado ao banco de dados
    user_db = mongo.db.usuarios.find_one({'username': username})
    assert user_db is not None
    assert check_password_hash(user_db['password'], password)




def test_user_exists_should_status_code_401(client):
    # Teste de registro de usuário válido
    username = 'usedsdsr1'
    password = '1234562322'
    user_data = {'username': username, 'password': password}
    response = client.post('/auth/signup', json=user_data)

    assert response.status_code == 401
    assert 'id' not in json.loads(response.data)

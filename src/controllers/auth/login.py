from datetime import timedelta
from datetime import datetime
from flask import request
from src import mongo
from src.decorators.log import log_wrapper
from src.decorators.validate.require_keys import require_keys_body
from werkzeug.security import check_password_hash
from src.models.entities.user import User

from src import app
import jwt


@app.route('/auth/login', methods=['POST'])
@require_keys_body(['username', 'password'])
@log_wrapper()
def login():
    user_payload = User(**request.json)

    user_authenticate = mongo.db.usuarios.find_one({"username": user_payload.username})

    if user_authenticate:
        if not check_password_hash(pwhash=user_authenticate['password'], password=user_payload.password):
            return {'message': 'Senha incorreta'}, 401
    else:
        return {'message': 'Usuario não existe'}, 401


    secret = app.config['SECRET_KEY']
    exp = datetime.utcnow() + timedelta(minutes=app.config['SESSION_EXPIRATE_MINUTES'])

    # Gera o token de acesso
    security_token = jwt.encode({
        'id': str(user_authenticate['_id']),
        'exp': exp,
        'username': user_payload.username,
    }, secret)

    return {'token': security_token, 'message': 'Usuario logado com sucesso'}, 200

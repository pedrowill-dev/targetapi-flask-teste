from src.models.entities.user import User
from src.decorators.validate.require_keys import require_keys_body
from werkzeug.security import generate_password_hash
from src.decorators.log import log_wrapper
from src import app
from flask import request
from src import mongo


@app.route('/auth/signup', methods=['POST'])
@require_keys_body(['username', 'password'])
@log_wrapper()
def signup():
    register_new = User(**request.json)

    user_exists = mongo.db.usuarios.find_one({"username": register_new.username})

    if user_exists:
        return {"message": "Usuário já cadastrado"}, 401

    try:
        password_hash = generate_password_hash(register_new.password)
    except:
        return {"message": f"Erro ao gerar senha - {register_new.password}"}, 500
    
    response_register_user = mongo.db.usuarios.insert_one({
        "username": register_new.username,
        "password": password_hash
    })

    response_register_new_id = str(response_register_user.inserted_id)

    return {"message": "Usuario registrado com sucesso", "id": response_register_new_id}, 201

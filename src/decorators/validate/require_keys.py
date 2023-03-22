from functools import wraps
from flask import request

def require_keys_body(keys):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            if not request.is_json:
                return {"message": "A solicitação deve conter um corpo JSON"}, 400
            
            data = request.get_json()
            
            for key in keys:
                if key not in data:
                    return {"message": f"A chave '{key}' é obrigatória no corpo JSON, campo invalido"}, 400         
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator











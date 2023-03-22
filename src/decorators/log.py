
from functools import wraps
from src import es_logger

def log_wrapper():
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            # Verifica se a resposta da função contém um token de acesso
            
            es_logger.info(result[0]['message'])
                # Faça algo com o token, se necessário
            return result
        return wrapper
    return decorator
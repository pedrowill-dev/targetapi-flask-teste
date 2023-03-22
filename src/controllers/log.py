import requests
from src import app
from src.config import ConfigurationElasticLog

@app.route('/logs', methods=['GET'])
def get_logging():
    response_log = requests.get(ConfigurationElasticLog.host)

    logs = []
    for log in response_log.json()['hits']['hits']:
        _log = log['_source']
        logs.append(_log)

    return logs

import os

class ConfigurationMongoDB:
    host = os.environ.get('MONGO_HOST', '127.0.0.1')
    port = 27017
    database = 'cep'

class ConfigurationAPICEP:
    host = 'https://viacep.com.br/'

class ConfigurationAPIInpe:
    host = 'http://servicos.cptec.inpe.br/XML/listaCidades'


class ConfigurationInspectioHTTPBIN:
    """Configuração de URLs de APIs externas."""
    host = 'http://httpbin.org/'



class ConfigurationLocationGEO:
    """Configuração de URLs de APIs externas."""
    host = 'http://ip-api.com/json/'


class ConfigurationElasticLog:
    host = f"{os.environ.get('ELASTIC_HOST', 'http://localhost:9200')}/logs_api/_search"
        

class LoggerConfigElasticsearch:
    host: str = os.environ.get('ELASTIC_HOST', 'http://localhost:9200')
    index_name: str = 'logs_api'

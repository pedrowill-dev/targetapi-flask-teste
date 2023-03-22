from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from src.config import LoggerConfigElasticsearch
from src.services.elasticsearch_log import ElasticSearchLogger
from flasgger import Swagger


es_logger = ElasticSearchLogger(
    index_name=LoggerConfigElasticsearch.index_name,
    elasticsearch_host=LoggerConfigElasticsearch.host)


app   = Flask(__name__)
app.config.from_object('config')
cors  = CORS(app)
ma    = Marshmallow(app)
mongo = PyMongo(app)
jwt   = JWTManager(app)
swagger = Swagger(app, template_file='doc.yaml')


from src.controllers.auth.signup import *
from src.controllers.auth.login import *
from src.controllers.cep.search import *
from src.controllers.log import *


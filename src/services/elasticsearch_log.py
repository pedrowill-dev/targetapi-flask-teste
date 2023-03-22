from elasticsearch import Elasticsearch
import logging


class ElasticSearchLogger(logging.Logger):

    def __init__(self, index_name, elasticsearch_host):
        super().__init__(index_name)
        self.es = Elasticsearch([elasticsearch_host])
        if not self.es.indices.exists(index=index_name):
            self.es.indices.create(index=index_name)


        self.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.addHandler(handler)
        self.index_name = index_name

    def log(self, level, message, extra=None):
        super().log(level, message, extra=extra)
        document = {
            'level': level,
            'message': message,
            'logger': self.index_name
        }
        if extra:
            document.update(extra)
        self.es.index(index=self.index_name, body=document)

    def info(self, message, extra=None):
        self.log(logging.INFO, message, extra=extra)

    def warning(self, message, extra=None):
        self.log(logging.WARNING, message, extra=extra)

    def error(self, message, extra=None):
        self.log(logging.ERROR, message, extra=extra)

    def critical(self, message, extra=None):
        self.log(logging.CRITICAL, message, extra=extra)

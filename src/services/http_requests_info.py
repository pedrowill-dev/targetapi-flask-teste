import requests as req
from src.config import ConfigurationInspectioHTTPBIN, ConfigurationLocationGEO


class HttpRequestInfo:

    def get_request_info(self, type_request, ip=None):

        http_requests_dict = {
            'user_agent': {
                'url': ConfigurationInspectioHTTPBIN.host +  'user-agent',
                'key': 'user-agent',
                'message': 'User-agent not found'
            },
            'ip': {
                'url': ConfigurationInspectioHTTPBIN.host +"ip",
                'key': 'origin',
                'message': 'Ip address not found'
            },
            'geo': {
                'url': ConfigurationLocationGEO.host + str(ip),
                'key': 'status',
                'message': 'Geo location not found'
            }
        }

        url, key, message = http_requests_dict[type_request].values()

        response_value_http = message
        response_http = req.get(url)
        response_http_json = response_http.json()

        if response_http_json.get(key):
            if type_request == 'geo':
                response_value_http = response_http_json
            else:
                response_value_http = response_http_json.get(key)
        return response_value_http

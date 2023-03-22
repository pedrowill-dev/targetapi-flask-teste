from flask import request
from src.decorators.auth.login_required import login_required
from src.decorators.validate.require_keys import require_keys_body
from src.config import ConfigurationAPICEP, ConfigurationAPIInpe
from src import app
from unidecode import unidecode
import requests
import xml.etree.ElementTree as ET
import xmltodict
import re
from src import es_logger
from src.services.http_requests_info import HttpRequestInfo

http_request_info = HttpRequestInfo()
ip = http_request_info.get_request_info('ip')
user_agent_info = http_request_info.get_request_info('user_agent')
geo_loc = http_request_info.get_request_info('geo', ip)
city_ip = geo_loc['city'] if geo_loc['city'] else 'Unknown'
provider = geo_loc['org'] if geo_loc['org'] else 'Unknown'

log = f'IP: {ip} - User-Agent: {user_agent_info} - Provider: {provider} - City: {city_ip}'


@app.route('/cep/search', methods=['POST'])
@login_required()
@require_keys_body(['cep'])
def search_cep(current_user):
    cep = request.json['cep']

    regex_cep = re.compile(r'^\d{8}$')

    if not regex_cep.match(cep):
        es_logger.warning(f'O CEP "{cep}" é inválido.')
        return {"message": f'O CEP "{cep}" é inválido.'}, 400

    request_cep = requests.get(
        f'{ConfigurationAPICEP.host}/ws/{cep}/json/').json()

    if request_cep.get('erro'):
        es_logger.warning(f'CEP não encontrado: {cep}')
        return {'message': f'CEP não encontrado: {cep}'}, 404

    city = request_cep['localidade']    

    city_formated = unidecode(city)
    cod_city = inpe_cod_city(city_formated, city)

    if cod_city is not None:
        request_inpe = requests.get(
            f'http://servicos.cptec.inpe.br/XML/cidade/{cod_city}/previsao.xml')
        response_inpe_json = xmltodict.parse(request_inpe.content)
        response_inpe_json.update({"info_cep": request_cep})
        es_logger.info(
            f'Consulta sucedida: {cep} - {log} - Codígo: {cod_city}')

        return response_inpe_json

    es_logger.warning(
        f'Consulta sucedida: {cep} - {log} - Codígo: {cod_city}')
    return {'message': f'Clima de 4 dias na cidade {city} não encontrada'}


def inpe_cod_city(city_formated, city):
    response = requests.get(
        ConfigurationAPIInpe.host,
        params={'city': city_formated})

    response_xml = ET.fromstring(response.content)
    codigo = None
    for cidade in response_xml.findall('cidade'):
        if cidade.findtext('nome') == city:
            codigo = cidade.findtext('id')
            break

    if codigo:
        return codigo
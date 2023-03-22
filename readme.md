# Projeto CEP e Clima

Este projeto é uma aplicação Flask que permite capturar um CEP através de uma requisição a uma API e, em seguida, retorna o clima dos próximos 4 dias. Ele utiliza Elasticsearch para gerar os logs das requisições e Docker como container.



### Pré-requisitos
Antes de executar a aplicação, é necessário ter instalado as seguintes ferramentas:

* Python 3: 
* Docker: 

### Como executar a aplicação
1. Clone o repositório em sua máquina local:<br>

  `git clone https://github.com/pedrowill-dev/targetdata-api-test-python`
  
2. Acesse o diretório do projeto:

  `cd targetdata-api-test-python`
  
3. Execute o comando para criar network no docker

  `docker network create network_bridge`
  
4. Executar o docker compose up

  `docker-compose up -d`
  

## Documentação de todos os endpoints da aplicação

> http://localhost:5000/apidocs


## Como utilizar a aplicação
Registre-se na plataforma
Para utilizar a API, primeiro é necessário se registrar na plataforma. Para isso, envie uma requisição POST para o endpoint `/auth/signup` com um payload contendo as informações de registro:

```json
{
    "username": "seu-usuario",
    "password": "sua-senha"
}
```

A resposta será um token de autenticação para ser utilizado nas requisições subsequentes:

```json
{
    "token": "seu-token"
}
```

Realize o login e obtenha a chave API
Para utilizar o endpoint de busca de previsão do tempo, é necessário realizar o login na plataforma e obter uma chave API. Para isso, envie uma requisição POST para o endpoint /auth/login com as informações de login:

```json
{
    "username": "seu-usuario",
    "password": "sua-senha"
}
```

A resposta será um token de autenticação para ser utilizado nas requisições subsequentes, incluindo a chave API:

```json
{
    "message": "Usuario logado com sucesso",
    "token": "seu-token"
}
```

## Busque a previsão do tempo a partir do CEP informado
Com a chave API em mãos, é possível realizar a busca da previsão do tempo para um CEP informado pelo usuário. Para isso, envie uma requisição `GET` para o endpoint `/cep/search` com o cabeçalho



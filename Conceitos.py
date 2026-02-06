# O que são APIs (Application Programming Interface - Interface de Programação de Aplicações)?!
# Analogia com um restaurante:
# 'fregueses' - Cliente (frontend, requisições de usuários); 'menu' - Documentação; 
# 'garçom' - API (intermediário, tratamento de requisições, tipo de backend); 
# 'cozinha' - Servidor/Banco de Dados.

# =-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# O que é REST (REpresentational State Transfer)?!
# Basicamente, trata do envio e recebimento de informações, através de métodos (Post, Get, Put, Delete);

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Representações e códigos de status HTTP:
# códigos de erro ou sucesso nas interações entre front e backend.

# * API RESTful - Um estilo de arquitetura para APIs que utiliza o protocolo HTTP para realizar operações de criação, 
# leitura, atualização e exclusão de dados, seguindo os princípios do "Representation State Transfer".

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# FastAPI:
# Frameworks - são como bibliotécas; mas são conjuntos de códigos mais robustos. 
# Frameworks conhecidos para o desenvolvimento com Python: Flask, Django e FastAPI. 
# instalação do FastAPI através do poetry shell; *poetry.lock mostra o que já foi salvo em nosso código*.

# Métodos HTTP:

# Post, Get, Put, Delete - essa estrutura, dentro de uma API, é chamada de CRUD (Creat, Read, Update, Delete).
# google.com.br, youtube.com.br... esses endereços são 'endpoints'

# Corpo da requisição HTTP: padrão - JSON

# Documentação Swagger - documentar os endpoints da nossa aplicação (da API)

# Autenticação: processo de identificar/autenticar a identidade do usuário no sistema.
# Autorização: restrições de acesso à informações ou a funções de um sistema ou aplicação.

# Métodos de autenticação do sistema: 
# JWT (JSON wbe token) - é um método onde o servidor 
# gera um token de autenticação com as informações do usuário.
# APIgateway - é uma ferramenta de proteção para aplicações web, que usa JWT.
# OAuth 2.0 - atenticação em ambientes externos (google, facebook...)

# O que é o FastAPI: é um framework moderno (2018), de alto desempenho e rápido de codificar, projetado
# para construir API's com Python, baseado em dicas de tipo padrão (type hints). Baseado em Starlette e
# Pydantic, oferece validação automática de dados, documentação interativa automática (Swagger UI) e
# suporte assíncrono, sendo ideal para microsserviços.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# O que é o fastapi.security: é um submódulo do fastapi projetado para simplificar a autenticação
# e autorização em API's. Ele oferece ferramentas prontas como OAuth2 e TokensJWT, que se integram à
# documentação interativa (Swagger UI), facilitando a proteção de rotas, verificação de identidade
# e controle de acesso a recursos, seguindo padrões OpenAPI.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# O que é o Pydantic: é a principal biblioteca Python para validação de dados e gerenciamento de 
# configurações, amplamente utilizada para garantir que os dados sigam um formato específico, 
# convertendo tipos automaticamente. Baseado em anotaçoes de tipo (type hints), ele é rápido, 
# extensível e fundamental em frameworks como o fastapi.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# O que é o Typing: 'typing' (digitação em inglês), refere-se ao ato de inserir dados, textos ou 
# comandos em dispositivos eletrônicos. No Python, refere-se ao uso de type hints (dicas de tipo)
# e ao módulo typing, permitindo especificar os tipos de dados (int, list, str...) de variáveis,
# parâmetros e retornos de funções. Introduzido para melhorar a legibilidade, documentação e detecção 
# de erros via ferramentas estáticas (como mypy), ele torna o código autodescritivo sem alterar a 
# execução dinâmica da linguagem.

# *Type hints: (anotações ou dicas de tipo) sintaxe para indicar tipos, ex.: def soma(a: int, b: int) -> int.
# *No terminal, para subir o código para o insomnia: fastapi dev main.py.

# Paginação: é feita apenas no GET.

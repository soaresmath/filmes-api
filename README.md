# Filmes API

Script em Python que consome a API do TMDB (The Movie Database) 
para buscar filmes e processar os dados retornados.

## O que faz
- Faz uma requisição HTTP à API do TMDB
- Recebe a resposta em JSON
- Processa e filtra os dados relevantes (título, ano, nota) de cada filme

## Tecnologias
- Python
- requests
- python-dotenv

## Como rodar
1. Clone o repositório
2. Crie um ambiente virtual e instale as dependências: `pip install requests python-dotenv`
3. Crie um arquivo `.env` com sua própria chave: `TMDB_API_KEY=sua_chave`
4. Execute: `python buscar_filmes.py`
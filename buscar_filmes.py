import requests
import os
from dotenv import load_dotenv


def processar_filmes(lista_filmes):
    filme_filtrado = []

    titulo = 0
    ano = 0
    nota = 0

    for resultado in lista_filmes["results"]:
        for label, dado in resultado.items():
            if   label == "title":
               titulo = dado

            elif label == "release_date":
                ano = dado[:4]

            elif label == "vote_average":
                nota = dado

        filme_filtrado.append({"titulo": titulo,"ano": ano,"nota": nota})

    return filme_filtrado

def busca_filmes(filme):
    load_dotenv() # lê o arquivo env, disponilizando as variaveis do arquivo

    api_key = os.getenv("TMDB_API_KEY") # pega a chave especifica do arquivo
    url = "https://api.themoviedb.org/3/search/movie"

    parametros = {
        "api_key": api_key,
        "query":   filme,
        "language": "pt-BR"
    }

    resposta = requests.get(url, params=parametros) 
    filmes = resposta.json() 

    return filmes

termo_busca = input("Digite o filme: ")

dados = busca_filmes(termo_busca)
filmes = processar_filmes(dados)

for filme in filmes:
    print(filme)

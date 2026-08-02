import requests
import json
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

    try:
        resposta = requests.get(url, params=parametros) 
        filmes = resposta.json() 
        return filmes
    except requests.exceptions.RequestException:
        print("Erro ao conectar com a API. Verifique sua internet")
        return None

def filtrar_por_nota(filmes, nota_minima):
    resultado = []
    for filme in filmes:
        if filme["nota"] >= nota_minima:
            resultado.append(filme)
    return resultado

filtros = {
    "1": ("Nota", lambda x: x["nota"]),
    "2": ("Ano de Lançamento", lambda x: x["ano"]),
}


while True:

    termo_busca = input("Digite o filme: ")
    dados = busca_filmes(termo_busca)

    if dados is None:
        print("Não foi possível buscar os filmes.")
        exit()

    filmes = processar_filmes(dados)

    flag = None

    while flag is None:
        try:

            for indice, filtro in filtros.items():
                print(f"{indice} = {filtro[0]}")

            print()
            print("Digite 'Sair' caso queira sem filtro")
            print()

            filtro_escolhido = input("Escolha um filtro: ")

            if filtro_escolhido != "Sair":

                filtro_key = filtros[filtro_escolhido][1]

                if filtros["1"][1] == filtro_key:
                    filtrar_nota = input('Deseja limitar notas: "Sim": ')
                    print()

                    filtrar_nota = filtrar_nota.upper()

                    if filtrar_nota == "SIM":
                        nota_minima = float(input("Nota minim:"))
                        filmes = filtrar_por_nota(filmes, nota_minima)
                    else:
                        print("Não limitado:")
                    
                filmes_ordenados = sorted(filmes, key=filtro_key, reverse=True)

                filmes = filmes_ordenados

            for filme in filmes:
                print(filme)

            flag = True
        except KeyError:
            print("Não existe esse filtro na listagem")
    print() 
    salvar_dados = input("Deseja salvar o dado dos filmes? (sim/não): ")

    salvar_dados = salvar_dados.upper()

    if salvar_dados != "NÃO" and salvar_dados != "NAO":
        with open(f"{termo_busca}.json", "w", encoding="utf-8") as arquivo:
            json.dump(filmes, arquivo, ensure_ascii=False, indent=2)

        print("Filmes salvos")

    print()
    continuar = input("Buscar outro filme? (sim/não): ").upper()
    if continuar != "SIM":
        break
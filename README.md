# Filmes API

Script em Python que consome a API do TMDB (The Movie Database) para 
buscar filmes, processar os dados e oferecer filtros e ordenação 
interativos direto no terminal.

## O que faz
- Busca filmes por nome, via input do usuário
- Consome a API do TMDB (requisição HTTP + tratamento de JSON)
- Processa e filtra os campos relevantes de cada filme (título, ano, nota)
- Permite ordenar os resultados por nota ou ano de lançamento (menu dinâmico)
- Permite filtrar por nota mínima
- Permite realizar múltiplas buscas na mesma execução
- Salva os resultados em arquivo JSON, sob demanda
- Trata erros de entrada inválida, filtro inexistente e falha de conexão com a API

## Tecnologias
- Python
- requests
- python-dotenv

## Como rodar
1. Clone o repositório
2. Crie um ambiente virtual e instale as dependências:
3. Crie um arquivo `.env` na raiz do projeto com sua própria chave:
4. Execute:

## Sobre o projeto
Este é um projeto de estudo, parte da Semana 2 de um roteiro de 
aprendizado autodidata em Python voltado para Engenharia de Dados. 
O código evoluiu de um script simples de consumo de API para uma 
ferramenta com processamento, filtros dinâmicos e tratamento de erros — 
todo o histórico de evolução está documentado nos commits.
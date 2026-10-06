import requests
import pandas as pd

# Método de pesquisa de livros
def busca(tipo, termo):
    url = "https://openlibrary.org/search.json"
    config_busca = {
        "sort": "old",  # mais antigos primeiro
        "limit": 100,
        "fields": "title,author_name,first_publish_year,subject"
    }
    match tipo:
        # Pesquisa por título
        case "titulo":
            config_busca["title"] = termo
        # Pesquisa por autor
        case "autor":
            config_busca["author"] = termo
        case _:
            return None

    resposta = requests.get(url, params=config_busca)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

# Transforma o JSON da API em uma tabela (DataFrame)
def para_tabela(dados):
    lista = []
    for livro in dados.get("docs", []):
        lista.append({
            "titulo": livro.get("title"),
            "autor": ", ".join(livro.get("author_name", ["Desconhecido"])),
            "ano": livro.get("first_publish_year"),
            # Usa o primeiro assunto (subject) como gênero
            "genero": livro.get("subject", ["Sem gênero"])[0]
        })
    return pd.DataFrame(lista, columns=["titulo", "autor", "ano", "genero"])

# Desafio 1: os 10 livros mais antigos da busca
def mais_antigos(df):
    return df.dropna(subset=["ano"]).sort_values("ano").head(10)
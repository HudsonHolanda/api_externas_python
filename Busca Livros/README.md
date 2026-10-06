# Sistema de Busca de Livros

Projeto simples em Python que busca livros pela **API da Open Library**, mostra os 10 mais antigos da pesquisa e gera gráficos de gêneros e anos de publicação.

## Funcionalidades

- Busca de livros por **título** ou **autor**
- Organização dos resultados em tabela (pandas)
- **Desafio 1:** exibe os 10 livros mais antigos da busca
- **Desafio 2:** gráfico com a quantidade de livros, gêneros mais comuns e livros por década

## Estrutura

```
.
├── main.py       # Arquivo principal (executa tudo)
├── busca.py      # Requisição à API e criação da tabela
├── graficos.py   # Geração dos gráficos
└── README.md
```

## Instalação

Requer Python 3.10 ou superior (usa `match/case`).

```bash
pip install requests pandas matplotlib
```

## Como usar

```bash
python main.py
```

Para mudar a pesquisa, edite a linha no `main.py`:

```python
# Por título
dados = busca.busca("titulo", "python")

# Por autor
dados = busca.busca("autor", "tolkien")
```

## Como funciona

| Arquivo | Função | O que faz |
|---|---|---|
| `busca.py` | `busca(tipo, termo)` | Faz a requisição à API com parâmetros e retorna o JSON |
| `busca.py` | `para_tabela(dados)` | Converte o JSON em um DataFrame (título, autor, ano, gênero) |
| `busca.py` | `mais_antigos(df)` | Retorna os 10 livros mais antigos |
| `graficos.py` | `gerar_grafico(df)` | Mostra os gráficos de gêneros e décadas |

## API utilizada

[Open Library Search API](https://openlibrary.org/dev/docs/api/search) — `https://openlibrary.org/search.json`

Parâmetros usados: `title` ou `author`, `sort=old`, `limit=100` e `fields`.

## Observações

- A Open Library não tem um campo de "gênero"; o projeto usa o primeiro **assunto (`subject`)** de cada livro.
- Livros sem ano de publicação ficam fora do ranking dos mais antigos.
- A busca traz no máximo 100 livros por pesquisa.

## Bibliotecas

- `requests` — requisições HTTP
- `pandas` — tabelas estruturadas
- `matplotlib` — gráficos
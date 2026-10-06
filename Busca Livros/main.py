import busca
import graficos

# Busca por título (troque por "autor" no primeiro parâmetro para pesquisar por autor)
dados = busca.busca("titulo", "python")

if dados is None or not dados.get("docs"):
    print("Nenhum livro encontrado.")
else:
    # Organiza os dados em uma tabela
    livros = busca.para_tabela(dados)

    # Desafio 1: 10 livros mais antigos
    print("10 livros mais antigos:")
    print(busca.mais_antigos(livros))

    # Desafio 2: gráfico de gêneros e anos
    graficos.gerar_grafico(livros)
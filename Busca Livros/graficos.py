import matplotlib.pyplot as plt

# Desafio 2: mostra quantidade de livros, gêneros e anos em gráfico
def gerar_grafico(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico 1: os 10 gêneros mais comuns
    df["genero"].value_counts().head(10).plot(
        kind="barh", ax=ax1, title="Gêneros mais comuns"
    )

    # Gráfico 2: quantidade de livros por década
    decadas = (df["ano"].dropna() // 10 * 10).astype(int)
    decadas.value_counts().sort_index().plot(
        kind="bar", ax=ax2, title="Livros por década"
    )

    # Quantidade total de livros no título
    fig.suptitle(f"Total de livros encontrados: {len(df)}")
    plt.tight_layout()
    plt.show()
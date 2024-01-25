from repositorio.livro_repositorio import livro_repositorio


def listarLivro() -> None:
    print("-- Todos Livros ----")

    for livro in livro_repositorio:
        print(f"Codigo:{livro['codigo']}")
        print(f"titulo: {livro['titulo']}")
        print(f"autor {livro['autor']}")
        print(f"emprestado? {livro['emprestado']}")
        print("-"*30)


if __name__ == "__main__":
    listarLivro()
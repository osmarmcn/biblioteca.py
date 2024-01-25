from repositorio.livro_repositorio import livro_repositorio

codigo_atual = 1

# function

def registro(titulo: str, autor: str) -> None:
    # para alterar uma variavel global dentro de uma funÇão, pois não é permitido está alteração sem o uso do global

    livro = criarlivro(titulo, autor)
    livro_repositorio.append(livro)
    print('livro adicionado com sucesso!')




def criarlivro(titulo: str, autor: str) -> dict:
    global codigo_atual
    codigo_atual += 1
    livro = {
        "codigo": codigo_atual,
        "titulo": titulo,
        "autor": autor,
        "emprestado": False
    }

    return livro

if __name__== "__main__":
    registro("1984", "George Orwel")
    print(livro_repositorio)
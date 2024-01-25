from repositorio.livro_repositorio import livro_repositorio

from livro.buscar import buscarCodigo


def editarLivro(codigo: int, titulo: str, autor: str) ->None:
    livro = buscarCodigo((codigo))

    if livro :
        livro['titulo'] = titulo
        livro['autor'] = autor
        print('dados alterados com sucesso!')

    else:
        print('livro não encotrado!')



if __name__ == "__main__":
    editarLivro(1,"Clean Code", "Arthur")
    print(buscarCodigo(1))
    editarLivro(2, "As Cronicas de narnia", "Wells")
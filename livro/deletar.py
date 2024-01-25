
from repositorio.livro_repositorio import livro_repositorio
from livro.buscar import  buscarCodigo

def deletarLivro(codigo: int) ->None:
    livro = buscarCodigo(codigo)
    if livro:
        livro_repositorio.remove(livro)
        print('livro removido com sucesso!')

    else:
        print("livro inexistente!")




if __name__ == "__main__":
    deletarLivro(1)
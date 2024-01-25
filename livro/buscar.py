from repositorio.livro_repositorio import livro_repositorio

def buscarCodigo(codigo: int) -> dict or None:
    for livro in livro_repositorio:
        if livro['codigo'] == codigo:
            return livro

    return None




if __name__ == "__main__":
    print(buscarCodigo(1))
    print(buscarCodigo(10))
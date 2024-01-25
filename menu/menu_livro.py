from livro.buscar import buscarCodigo
from livro.editar import editarLivro
from livro.listar import listarLivro
from livro.deletar import deletarLivro
from livro.registrar import registro


def menu() -> None:
    while True:
      print("--- seja bem-vindo!---")

      op = int(input('escolha sua opção: '))

      if op == 1:
          titulo = input('digite seu titulo: ')
          autor = input('digite o autor: ')
          registro(titulo,autor)

      elif op == 2:
          codigo = int(input('digite o codigo: '))
          titulo = input('digite seu titulo: ')
          autor = input('digite o autor: ')
          editarLivro(codigo, titulo, autor)

      elif op == 3:
          codigo = int(input('digite o codigo: '))
          deletarLivro(codigo)

      elif op == 4:
          codigo = int(input('digite o codigo: '))
          buscarCodigo(codigo)

      elif op == 5:
          listarLivro()

      else:
          break



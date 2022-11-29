from telas import *
from persistencia import *


def menu():
    limparTela()
    print("-------- Sistema de Produtos --------")
    print("1 - Cadastrar Produto")
    print("2 - Editar Produto")
    print("3 - Excluir Produto")
    print("4 - Selecionar Produto")
    print("5 - Listar Produtos")
    print("6 - Sair")
    print("-------------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


while True:
    opcao = menu()

    if opcao == 1:
        produto = cadastrarProduto()
        criar(produto)
        exibirMsg("Produto cadastrado com sucesso!")
    elif opcao == 2:
        produto = editarProduto()
        editar(produto)
        exibirMsg("Produto editado com sucesso!")
    elif opcao == 3:
        limparTela()
        id = excluirProduto()
        excluir(id)
        exibirMsg("Produto excluído com sucesso!")
    elif opcao == 4:
        id = selecionarProduto()
        produto = selecionar(id)
        if produto == None:
            exibirMsg("Produto não encontrado!")
        else:
            exibirProduto(produto)
            travarTela()
    elif opcao == 5:
        produtos = selecionar_todos()
        exibirProdutos(produtos)
    elif opcao == 6:
        break

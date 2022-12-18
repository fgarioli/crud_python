from telas import *
from persistencia import Persistencia


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


persistencia = Persistencia()

while True:
    opcao = menu()

    if opcao == 1:
        produto = cadastrarProduto()
        persistencia.criar(produto)
        exibirMsg("Produto cadastrado com sucesso!")
    elif opcao == 2:
        produto = editarProduto()
        persistencia.editar(produto)
        exibirMsg("Produto editado com sucesso!")
    elif opcao == 3:
        limparTela()
        id = excluirProduto()
        persistencia.excluir(id)
        exibirMsg("Produto excluído com sucesso!")
    elif opcao == 4:
        id = selecionarProduto()
        produto = persistencia.selecionar(id)
        if produto == None:
            exibirMsg("Produto não encontrado!")
        else:
            exibirProduto(produto)
            travarTela()
    elif opcao == 5:
        produtos = persistencia.selecionar_todos()
        exibirProdutos(produtos)
    elif opcao == 6:
        break

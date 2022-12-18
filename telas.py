import os
from Produto import Produto


def cadastrarProduto() -> Produto:
    limparTela()
    print("-------- Cadastro de Produto --------")
    produto = Produto()
    produto.setNome(input('Nome: '))
    produto.setPreco(float(input('Preço: ')))
    produto.setQuantidade(int(input('Quantidade: ')))

    return produto


def editarProduto() -> Produto:
    limparTela()
    print("-------- Edição de Produto --------")
    produto = Produto()
    produto.setId(int(input('Id: ')))
    produto.setNome(input('Nome: '))
    produto.setPreco(float(input('Preço: ')))
    produto.setQuantidade(int(input('Quantidade: ')))

    return produto


def excluirProduto():
    print("-------- Exclusão de Produto --------")
    limparTela()
    id = int(input('Id: '))
    return id


def selecionarProduto():
    limparTela()
    print("-------- Seleção de Produto --------")
    id = int(input('Id: '))
    return id


def exibirProduto(produto: Produto):
    print("-------- Produto --------")
    print(f"Id: {produto.getId()}")
    print(f"Nome: {produto.getNome()}")
    print(f"Preço: {produto.getPreco()}")
    print(f"Quantidade: {produto.getQuantidade()}")


def exibirProdutos(produtos):
    limparTela()
    print("---------------- Produtos ----------------")
    for produto in produtos:
        exibirProduto(produto)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para continuar...')


def exibirMsg(msg):
    print(msg)
    travarTela()

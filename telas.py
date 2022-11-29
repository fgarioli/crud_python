import os


def cadastrarProduto():
    limparTela()
    print("-------- Cadastro de Produto --------")
    produto = {}
    produto['nome'] = input('Nome: ')
    produto['preco'] = float(input('Preço: '))
    produto['quantidade'] = int(input('Quantidade: '))

    return produto


def editarProduto():
    limparTela()
    print("-------- Edição de Produto --------")
    produto = {}
    produto['id'] = int(input('Id: '))
    produto['nome'] = input('Nome: ')
    produto['preco'] = float(input('Preço: '))
    produto['quantidade'] = int(input('Quantidade: '))

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


def exibirProduto(produto):
    print("-------- Produto --------")
    print(f"Id: {produto['id']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: {produto['preco']}")
    print(f"Quantidade: {produto['quantidade']}")


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

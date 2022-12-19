from json_storage import JsonStorage
from Produto import Produto


class Persistencia():
    __storage = JsonStorage()

    def criar(self, dado: Produto) -> Produto:
        dados = self.selecionar_todos()
        dado.setId(self.__gerarId())
        dados.append(dado)
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def editar(self, dado: Produto) -> None:
        dados = self.selecionar_todos()
        for i, data in enumerate(dados):
            if data.getId() == dado.getId():
                dados[i] = dado
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def excluir(self, id: int) -> None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                dados.remove(dado)
        self.__storage.gravarJson(dados)

    def selecionar(self, id: int) -> Produto | None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                return dado
        return None

    def selecionar_todos(self) -> list[Produto]:
        produtos = []
        for i in self.__storage.lerJson():
            produto = Produto()
            produto.setId(i['id'])
            produto.setNome(i['nome'])
            produto.setPreco(i['preco'])
            produto.setQuantidade(i['quantidade'])
            produtos.append(produto)
        return produtos

    def __gerarId(self) -> int:
        dados = self.selecionar_todos()
        if len(dados) == 0:
            return 1
        return dados[-1].getId() + 1

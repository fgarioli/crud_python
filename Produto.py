class Produto():
    __id: int
    __nome: str
    __preco: float
    __quantidade: int

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getPreco(self):
        return self.__preco

    def setPreco(self, preco):
        self.__preco = preco

    def getQuantidade(self):
        return self.__quantidade

    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade

    def toDict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'preco': self.__preco,
            'quantidade': self.__quantidade
        }

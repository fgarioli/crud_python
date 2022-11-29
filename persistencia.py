from json_storage import lerJson, gravarJson


def criar(dado: dict) -> dict:
    dados = lerJson()
    dado['id'] = gerarId()
    dados.append(dado)
    gravarJson(dados)


def editar(dado: dict) -> None:
    dados = lerJson()
    for i, data in enumerate(dados):
        if data['id'] == dado['id']:
            dados[i] = dado
    gravarJson(dados)


def excluir(id: int) -> None:
    dados = lerJson()
    for dado in dados:
        if dado['id'] == id:
            dados.remove(dado)
    gravarJson(dados)


def selecionar(id: int) -> dict | None:
    dados = lerJson()
    for dado in dados:
        if dado['id'] == id:
            return dado
    return None


def selecionar_todos() -> list:
    return lerJson()


def gerarId() -> int:
    dados = lerJson()
    if len(dados) == 0:
        return 1
    return dados[-1]['id'] + 1

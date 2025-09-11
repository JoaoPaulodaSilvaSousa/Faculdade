from collections import deque

grafo = {
    'voce': ['bob', 'alice', 'clarice'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'clarice': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

def pesquisa(nome):
    fila_de_pesquisa = deque(grafo[nome])  # já inicializa a fila
    verificadas = set()  # mais rápido que lista

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if pessoa.startswith('p'):  # começa com 'p'
                print(f"{pessoa} é quem procuramos!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.add(pessoa)
    return False

pesquisa("voce")

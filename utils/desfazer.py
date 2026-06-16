"""
Pilha para controle de historico
"""
class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Historico:
    def __init__(self):
        self.topo = None

    def vazia(self):
        return self.topo is None

    def push(self, operacao):
        novo = Node(operacao)
        novo.prox = self.topo
        self.topo = novo

    def pop(self):
        if self.vazia():
            return None

        operacao = self.topo.dado
        self.topo = self.topo.prox
        return operacao

    def topo_pilha(self):
        if self.vazia():
            return None

        return self.topo.dado
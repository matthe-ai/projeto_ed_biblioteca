class Fila:
    def __init__(self):
        self.dados = []

    def enfileirar(self, dado):
        self.dados = self.dados.append(dado)

    def desenfileirar(self):
        if len(self.dados) > 0:
            tmp = self.dados[0]
            for i in range(len(self.dados)-1):
                self.dados[i] = self.dados[i+1]
            self.dados = self.dados[:-1]
            return tmp
        else:
            return
    
    def vazia(self)->bool:
        if self.dados == []:
            return True
        else:
            return False

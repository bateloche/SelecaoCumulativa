class Reproducao:

    def __init__(self, pai, mutacao):
        self.pai = pai
        self.mutacao = mutacao

    def criar_geracao(self, quantidade_de_filhos):
        geracao = []
        for _ in range(quantidade_de_filhos):
            filho = self.mutacao.mutar(self.pai)
            geracao.append(filho)

        return geracao
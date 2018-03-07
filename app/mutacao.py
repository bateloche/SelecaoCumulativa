from random import SystemRandom
from string_utils import caracteres_possiveis

class Mutacao:

    def __init__(self, mutacoes):
        self.quantidade_mutacoes = mutacoes
        self.random = SystemRandom()
        self.caracteres = caracteres_possiveis()

    def mutar(self, texto):
        lst = list(texto)
        for _ in range(self.quantidade_mutacoes):
            novo_caractere = self.__caractere_aleatorio__()
            posicao = self.random.randint(0, len(texto) - 1)
            lst[posicao] = novo_caractere

        return ''.join(lst)

    def __caractere_aleatorio__(self):
        aleatorio = self.random.randint(0, len(self.caracteres) - 1)
        return self.caracteres[aleatorio]
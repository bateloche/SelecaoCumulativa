from random import randint
from string_utils import caracteres_possiveis

class GeradorStrings():

    def nova(self, comprimento):,
        caracteres = caracteres_possiveis()
        resultado = []
        for _ in range(comprimento):
            aleatorio = randint(0, len(caracteres) - 1)
            resultado.append(caracteres[aleatorio])

        return ''.join(resultado)
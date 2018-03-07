from random import randint
from str_comp import StrComp

class GeradorStrings():

    def nova(self, comprimento):
        comp = StrComp()
        caracteres = comp.CARACTERES_POSSIVEIS
        resultado = []
        for _ in range(comprimento):
            aleatorio = randint(0, len(caracteres) - 1)
            resultado.append(caracteres[aleatorio])

        return ''.join(resultado)
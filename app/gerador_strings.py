from random import randint
from compara_texto import ComparaTexto

class GeradorStrings():

    def nova(self, comprimento):
        comp = ComparaTexto()
        caracteres = comp.CARACTERES_POSSIVEIS()
        resultado = []
        for _ in range(comprimento):
            aleatorio = randint(0, len(caracteres) - 1)
            resultado.append(caracteres[aleatorio])

        return ''.join(resultado)
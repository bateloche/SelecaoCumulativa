from random import randint

class GeradorStrings():

    caracteres = "ABCDEFGHIJKLMNOPQRSTUWVXYZ "
    
    def nova(self, comprimento):
        resultado = []
        for _ in range(comprimento):
            aleatorio = randint(0, len(self.caracteres) - 1)
            resultado.append(self.caracteres[aleatorio])

        return ''.join(resultado)
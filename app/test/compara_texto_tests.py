import unittest
from compara_texto import ComparaTexto

class ComparaTextoTests(unittest.TestCase):

    def test_deve_retornar_zero_para_strings_iguais(self):
        comp = ComparaTexto()
        texto = "ABCDEFGH"
        diff = comp.caracteres_diferentes(texto, texto)
        self.assertEquals(0, diff)

    def test_deve_retornar_quantidade_de_caracteres_diferentes(self):
        texto = "ABCDEFGH"
        texto_2 = "IJCDEFGH"
        comp = ComparaTexto()
        diff = comp.caracteres_diferentes(texto, texto_2)
        self.assertEquals(2, diff)

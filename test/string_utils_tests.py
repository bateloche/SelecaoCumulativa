import unittest
from app.string_utils import caracteres_diferentes

class StringUtilsTests(unittest.TestCase):

    def test_deve_retornar_zero_para_strings_iguais(self):
        texto = "ABCDEFGH"
        diff = caracteres_diferentes(texto, texto)
        self.assertEquals(0, diff)

    def test_deve_retornar_quantidade_de_caracteres_diferentes(self):
        texto = "ABCDEFGH"
        texto_2 = "IJCDEFGH"
        diff = caracteres_diferentes(texto, texto_2)
        self.assertEquals(2, diff)

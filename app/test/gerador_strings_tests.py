import unittest
from gerador_strings import GeradorStrings

class GeradorStringsTests(unittest.TestCase):

    def test_deve_gerar_string_aleatoria_com_tamanho_solicitado(self):
        gerador = GeradorStrings()
        result = gerador.nova(28)
        self.assertEqual(28, len(result))

    def test_string_gerada_deve_ser_aleatoria(self):
        gerador = GeradorStrings()
        result = gerador.nova(28)
        other_result = gerador.nova(28)
        self.assertNotEqual(result, other_result)
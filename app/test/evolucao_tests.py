import unittest
from evolucao import Evolucao

class EvolucaoTests(unittest.TestCase):

    def test_aceita_quantidade_de_filhos_por_geracao(self):
        evo = Evolucao(10, "")
        self.assertEqual(10, evo.filhos_por_geracao)

    def test_aceita_texto_esperado_na_construcao(self):
        evo = Evolucao(1, "Hello World")
        self.assertEqual(evo.texto_esperado, "Hello World")
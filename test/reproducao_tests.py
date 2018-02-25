import unittest
from unittest.mock import Mock
from app.reproducao import Reproducao
from app.mutacao import Mutacao

class ReproducaoTests(unittest.TestCase):

    pai = "ABCDEFGHIJ"
    numero_de_filhos = 10
    mutacao_padrao = Mutacao(1)

    def test_deve_aceitar_pai_no_construtor(self):
        reproducao = Reproducao(self.pai, self.mutacao_padrao)
        self.assertEqual(self.pai, reproducao.pai)

    def test_deve_criar_nova_geracao_com_numero_de_filhos_esperados(self):
        reproducao = Reproducao(self.pai, self.mutacao_padrao)
        geracao = reproducao.criar_geracao(self.numero_de_filhos)
        self.assertEqual(10, len(geracao))

    def test_deve_mutar_cada_membro_da_nova_geracao(self):
        mutacao = Mutacao(1)
        mock = Mock()
        mutacao.mutar = mock
        reproducao = Reproducao(self.pai, mutacao)
        geracao = reproducao.criar_geracao(self.numero_de_filhos)
        self.assertEqual(self.numero_de_filhos, mock.call_count)

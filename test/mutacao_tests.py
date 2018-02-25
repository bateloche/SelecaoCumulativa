import unittest
from app.mutacao import Mutacao

class MutacaoTests(unittest.TestCase):

    def test_deve_aceitar_quantidade_de_mutacoes(self):
        mutacao = Mutacao(2)
        self.assertEqual(2, mutacao.quantidade_mutacoes)

    def test_deve_alterar_exatamente_a_quantidade_de_caracteres_solicitada_2(self):
        #Teste ruim!
        #Tanto este teste quanto o teste abaixo não são independentes
        #A maneira correta de efetuar estes testes seria injetar um encapsulamento
        #da class SystemRandom e validar a quantidade de chamadas em um mock
        #Estes testes falham eventualmente por colisões na geração de números aleatórios
        original = "ABCDEFGHIJKLMOPQ"
        mutacao = Mutacao(2)
        mutante = mutacao.mutar(original)
        self.assertEqual(2, self.caracteres_diferentes(original, mutante))

    def test_deve_alterar_exatamente_a_quantidade_de_caracteres_solicitada_1(self):
        original = "ABCDEFGHIJKLMOPQ"
        mutacao = Mutacao(1)
        mutante = mutacao.mutar(original)
        self.assertEqual(1, self.caracteres_diferentes(original, mutante))

    def caracteres_diferentes(self, texto, texto_alterado):
        diff = 0
        for i, c in enumerate(texto):
            if c != texto_alterado[i]:
                diff += 1
        
        return diff
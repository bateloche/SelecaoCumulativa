from compara_texto import ComparaTexto
from gerador_strings import GeradorStrings
from reproducao import Reproducao
from mutacao import Mutacao
from heapq import heappop, heappush, heapify

class Evolucao:

    def __init__(self, filhos_por_geracao, texto_esperado):
        self.filhos_por_geracao = filhos_por_geracao
        self.texto_esperado = texto_esperado

    def inicia(self):
        gerador = GeradorStrings()
        inicio = gerador.nova(len(self.texto_esperado))
        comp = ComparaTexto()
        atual = inicio
        mutacao = Mutacao(2)
        i = 1
        while atual != self.texto_esperado:
            reproducao = Reproducao(atual, mutacao)
            nova_geracao = reproducao.criar_geracao(self.filhos_por_geracao)
            analise = []
            for filho in nova_geracao:
                heappush(analise, (comp.caracteres_diferentes(filho, self.texto_esperado), filho))
            atual = heappop(analise)[1]
            print('Melhor filho: ' + atual)
            i += 1
            print('Geração: ' + str(i))
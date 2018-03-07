from gerador_strings import GeradorStrings
from reproducao import Reproducao
from mutacao import Mutacao
from heapq import heappop, heappush, heapify
from str_comp import StrComp

gerador = GeradorStrings()
fim = input().strip() # "METHINKS IT IS LIKE A WEASEL"
inicio = gerador.nova(len(fim))
comp = StrComp()

atual = inicio
mutacao = Mutacao(2)
i = 1
while atual != fim:
    reproducao = Reproducao(atual, mutacao)
    nova_geracao = reproducao.criar_geracao(500)
    analise = []
    for filho in nova_geracao:
        heappush(analise, (comp.caracteres_diferentes(filho, fim), filho))
    atual = heappop(analise)[1]
    print('Melhor filho: ' + atual)
    i += 1
    print('Geração: ' + str(i))
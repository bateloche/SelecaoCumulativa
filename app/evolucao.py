from gerador_strings import GeradorStrings
from reproducao import Reproducao
from mutacao import Mutacao
from heapq import heappop, heappush, heapify

def caracteres_diferentes(texto, texto_alterado):
    diff = 0
    for i, c in enumerate(texto):
        if c != texto_alterado[i]:
            diff += 1
        
    return diff

if __name__ == "__main__":
    gerador = GeradorStrings()
    fim = "METHINKS IT IS A WEASEL"
    inicio = gerador.nova(len(fim))

    atual = inicio
    mutacao = Mutacao(2)
    i = 1
    while atual != fim:
        reproducao = Reproducao(atual, mutacao)
        nova_geracao = reproducao.criar_geracao(1000)
        analise = []
        for filho in nova_geracao:
            heappush(analise, (caracteres_diferentes(filho, fim), filho))
        atual = heappop(analise)[1]
        print('Melhor filho: ' + atual)
        i += 1
        print('Geração: ' + str(i))
        
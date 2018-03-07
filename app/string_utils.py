def caracteres_diferentes(texto, texto_alterado):
    diff = 0
    for i, c in enumerate(texto):
        if c != texto_alterado[i]:
            diff += 1
        
    return diff

def caracteres_possiveis():
    return "ABCDEFGHIJKLMNOPQRSTUWVXYZ "
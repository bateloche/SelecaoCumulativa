class ComparaTexto():

    def caracteres_diferentes(self, texto, texto_alterado):
        diff = 0
        for i, c in enumerate(texto):
            if c != texto_alterado[i]:
                diff += 1
            
        return diff

    def CARACTERES_POSSIVEIS(self):
        return "ABCDEFGHIJKLMNOPQRSTUWVXYZ "
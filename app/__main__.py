from evolucao import Evolucao

if __name__ == "__main__":
    # "METHINKS IT IS LIKE A WEASEL"
    print("Texto esperado: ")
    texto_final = input().strip()
    evolucao = Evolucao(1000, texto_final)
    evolucao.inicia()
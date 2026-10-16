# Exemplo - Vogal ou consoante
# Aluna: Luiza Vieira
# Objetivo: Ler ums letra e informar se ela é vogal ou consoante

letra = str(input("Digite a sua letra: ")) #recebe, lê e armazena em letra

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u": #condição se a letra digitada for, a, e, i ou u
    print("Sua letra é uma vogal")  #exibe que é uma vogal
else:
    print("Sua letra é uma consoante") #se não exibe que é uma consoante


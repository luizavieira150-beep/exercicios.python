# Exemplo - Positivo, negativo ou zero
# Aluna: Luiza Vieira
# Objetivo: Ler o número e informar se é positivo negativo ou zero

num = int(input("Digite seu número: ")) # recebe lê e armazena em num

if num > 0: # condição maior que zero
    print("Número positivo") # exibe que o número é positivo
elif num < 0: # condição menor que zero
    print("Número negativo") # exibe que o número é negativo
else:
    print("Zero") # se não exibe que é zero
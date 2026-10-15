# Exemplo - Par ou ímpar
# Aluna: Luiza Vieira
# Objetivo: Ler e informar se é par ou ímpar

num = float(input("Digite seu número: ")) #lê e armazena em num
if num % 2 == 0: #condição se o resto da divizão for exatamente igual a zero
    print("Seu número é par") #exibe que o número é par
else:
    print("Seu número é ímpar") #senao exibe que o número é ímpar

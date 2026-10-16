# Exemplo - O maior de três
# Aluna: Luiza Vieira
# Objetivo: Ler e informar qual dos três é maior

num1 = int(input("Digite seu primeiro número: ")) #recebe, lê e armazena me num1
num2 = int(input("Digite seu segundo número: ")) #recebe, lê e armazena em num2
num3 = int(input("Digite seu terceiro número: ")) #recebe, lê e armazena em num3

if num1 > num2 and num1 > num3: #condição se o num1 for maior que num2 e num3
    print("O maior é", num1) #exibe que num1 é o maior
elif num2 > num1 and num2 > num3: #condição se não se o num2 for maior que num1 e num3
    print("O maior é", num2) #exibe que num2 é maior
else:
    print("O maior é", num3) #se não exibe que o num3 é o maior
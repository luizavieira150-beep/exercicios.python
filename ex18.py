# Exemplo - Maior ou iguais
# Aluna: Luiza Vieira
# Objetivo: Ler dois número e mostrar qual o maior ou se são iguais

num1 = int(input("Digite seu primeiro número: ")) #recebe lê e armzena em num1
num2 = int(input("Digite seu segundo número: ")) #recebe le e armazena em num2

if num1 > num2: #condição num1 maior que num2
    print("O maior é ", num1) #exibe que num1 é maior
elif num1 < num2: #condição num2 maior que num1
    print("O maior é ", num2) #exibe que num2 é maior
else:
    print("Os números são iguais") #se não exibe que os dois são iguais 
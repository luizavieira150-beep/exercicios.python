# Exemplo - Calculadora
# Aluna: Luiza Vieira
# Objetivo: Ler dois números e mostrar o resultado da operação

num1 = float(input("Digite seu primeiro número: ")) #le e armazena o primeiro número em num1
num2 = float(input("Digite seu segundo número: ")) #le e armazena em num2
oper = str(input("Digite o operador (+, -, * ou /):  ")) #le e armazena em oper

if oper == "+": #condição operador +
    resultado = num1 + num2 #faz conta de mais
    print("Resultado: ", resultado) #exibe resultado
elif oper == "-": #condição operador -
    resultado = num1 - num2 #faz conta de menos
    print("Resultado: ", resultado) #exibe resultado
elif oper == "*": #condição operador *
    resultado = num1 * num2 #faz conta de vezes
    print("Resultado: ", resultado) #exibe resultado
elif oper == "/" and num2 == 0: #se o num2 for igual a zero
    print("Erro: divisão por zero") #exibe erro
elif oper == "/": #condição operador /
    resultado = num1 / num2 #faz conta de divisão
    print("Resultado: ", resultado) #exibe resultado
else: 
    print("Operador inválido") #se não exibe operador inválido

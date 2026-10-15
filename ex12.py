# Exemplo - Divisão segura
# Aluna: Luiza Vieira
# Objetivo: Ler o dividendo e divisor e informar se existe divisão ou não

num1 = float(input("Digite seu dividendo: ")) # digita o dividendo, lê e armazena em num1
num2 = float(input("Digite seu divisor: ")) # digita o divisor, lê e armazena em num2

resultado = num1 / num2 # resultado da divisão fica armazenado em resultado

if num2 == 0: # condição, se o divisor for exatamente igual a zero
    print ("Erro: Não existe divisão") # exibe mensagem de erro
else:
    print("Resultado ", resultado) # se não exibe o resultado
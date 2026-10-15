# Exemplo - Desconto na compra
# Aluna: Luiza Vieira
# Objetivo: Ler o valor da compra e mostrar o valor final a pagar

valor = float(input("Digite o valor da sua compra: ")) #recebe, lê e armazena em valor
if valor >= 100.00: # 
    valorFim = valor - (valor * 0.10) # condição se o valor for maior ou igual a 100
    print ("Valor final: R$", valorFim) # faz a conta de desconto
else:
    print("Valor final: R$", valor) # se não exibe o valor normal
# Exemplo - Saque no caixa eletrônico
# Aluna: Luiza Vieira
# Objetivo: Ler o saldo que o usuário quer sacar e exibir se é suficiente ou não

saldo = float(input("Digite seu saldo atual: ")) # recebe, lê e armazena em saldo

valor = float(input("Digite o valor que deseja sacar: ")) # recebe, lê e armazena em valor

if valor < saldo: # condição se o valor for menor que o saldo
    valorAtual = saldo - valor # subtrai o valor que quer sacar pelo valor em onta e armazena em valorAtual
    print("Saque finalizado. Novo saldo: R$", valorAtual) # exibe mensagem de saque realizado e valor atual
else: 
    print("Saldo insuficiente.") # se não exibe saldo insuficiente
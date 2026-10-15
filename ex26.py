# Exemplo - Desconto progressivo
# Aluna: Luiza Vieira
# Objetivo: Ler o valor de uma compra e aplicar o desconto correnspondente

valor = float(input("Adicione o valor da sua compra: ")) #recebe, lê e armazena em valor 

if valor < 50: #condição se o valor for menor que 50
    print("Sem desconto") #exibe a mensagem sem desconto
elif valor < 100: #se não se o valor for menor que 100
    desconto = valor * 0.5 #calcula desconto
    valorFim = valor - desconto #calcula valor final
    print("Desconto: R$ ", desconto, "- Final: R$", valorFim) #exibe a mensagem final
elif valor < 200: #se não se o valor for menor que 200
    desconto = valor * 0.10 #calcula o desconto
    valorFim = valor - desconto #calcula o valor final
    print("Desconto: R$ ", desconto, "- Final: R$", valorFim) #exibe a mensagem final
else:
    desconto = valor * 0.15 #se não calcula o desconto de 15%
    valorFim = valor - desconto #calcula o valor final
    print("Desconto: R$ ", desconto,"- Final: R$", valorFim) #exibe a mensagem final

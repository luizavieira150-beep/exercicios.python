# Exemplo - Compra na cantina
# Aluna: Luiza Vieira
# Objetivo: Ler o preço do lanche, qtd comprada e valor pago, no final mostrar o total e o troco

preco = float(input("Digite o preço: ")) #lê preço e armazena em preco
qtd = float(input("Digite a quantidade: ")) #lê quantidade e armazena em qtd
valor = float(input("Digite o valor pago: ")) #lê valor e armazena em valor

total = preco * qtd #multiplica o preço e quantidade e da o resultado do total
troco = valor - total #o valor pago pelo total da compra para gerar o troco

print("Total: ", total, "Troco: ", troco) #exibe o total e o troco
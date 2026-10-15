# Exemplo - Cardápio da cantina
# Aluna: Luiza Vieira
# Objetivo: Mostrar o cardápio, ler o código do produto, a quantidade e o valor total

print("Cardápio da cantina \n") #exibe o cardápio
print("1 - Pão de queijo -R$ 4.50\n")
print("2 - Coxinha - R$ 6.00\n")
print("3 - Pastel - R$ 7.00\n")
print("4 - Suco - R$ 5.00\n")
print("5 - Cafe - R$ 3.00\n")

cod = int(input("Digite o código: ")) #recebe o código, lê e armazena em cod

if cod ==1: #condição se o codigo for igual a 1
    quantidade = int(input("Digite a quantidade: ")) #recebe a quantidade
    total = 4.50 * quantidade #calcula o total do pao de queijo
    print("Total: R$ ", total)
elif cod ==2: #condição se não se o codigo for igual a 2
    quantidade = int(input("Digite a quantidade: ")) #recebe a quantidade
    total = 6.00 * quantidade #calcula o total da coxinha
    print("Total: R$ ", total)
elif cod == 3: #condição se não se o codigo for igual a 3
    quantidade = int(input("Digite a quantidade: ")) #recebe a quantidade
    total = 7.00 * quantidade #calcula o total do pastel
    print("Total: R$ ", total)
elif cod == 4: #condição se não se o codigo for igual a 4
    quantidade = int(input("Digite a quantidade: ")) #recebe a quantidade
    total = 5.00 * quantidade #calcula o total do suco
    print("Total: R$ ", total)
elif cod == 5: #condição se não se o codigo for igual a 5
    quantidade = int(input("Digite a quantidade: ")) #recebe a quantidade
    total = 3.00 * quantidade #calcula o total do cafe
    print("Total: R$ ", total)
else:
    print("Código inválido") #se não exibe codigo invalido
# Exemplo - Três números em ordem crescente
# Aluna: Luiza Vieira
# Objetivo: Ler três números e mostrar eles em ordem crescente

num1 = int(input("Digite o primeiro número: ")) #le e armazena em num1
num2 = int(input("Digite o segundo número: ")) #le e armazena em num2
num3 = int(input("Digite o terceiro número: ")) #le e armazena em num3

if num1 <= num2 and num2 <= num3:
    print(f"Ordem: {num1} {num2} {num3}")
elif num1 <= num3 and num3 <= num2:
    print(f"Ordem: {num1} {num3} {num2}")
elif num2 <= num1 and num1 <= num3:
    print(f"Ordem: {num2} {num1} {num3}")
elif num2 <= num3 and num3 <= num1:
    print(f"Ordem: {num2} {num3} {num1}")
elif num3 <= num2 and num2 <= num1:
    print(f"Ordem: {num3} {num2} {num1}")
else:
    print(f"Ordem: {num3} {num1} {num2}")
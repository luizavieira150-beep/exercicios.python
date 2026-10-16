# Exemplo - Tipo de triângulo
# Aluna: Luiza Vieira
# Objetivo: Ler os três lados de um triângulo. E verificar seu tipo

lado1 = int(input("Digite o primeiro lado: ")) #recebe, le e armazena em lado1
lado2 = int(input("Digite o segundo lado: ")) #recebe, le e armazena em lado2
lado3 = int(input("Digite o terceiro lado: ")) #recebe, le e armazena em lado3

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3: #condição se forem todos iguais
    print("Equilátero") #exibe equilátero
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: #se forem apenas dois lados iguais
    print("Isósceles") #exibe isósceles
elif lado1 != lado2 or lado1 != lado3 or lado2 != lado3: #se forem todos diferentes
    print("Escaleno") #exibe escaleno
else:
    print("Esses lados não formam um triângulo") #se não exibe quenão forma um triângulo
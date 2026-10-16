# Exemplo - Equação do 2° grau
# Aluna: Luiza Vieira
# Objetivo: Ler os coeficientes a, b e c, e resolva

a = int(input("Digite seu coeficiente a: ")) #recebe, lê e armazena em a
b = int(input("Digite seu coeficiente b: ")) #recebe, lê e armazena em b
c = int(input("Digite seu coeficiente c: ")) #recebe, lê e armazena em c

delta = b**2 - 4 * a * c #conta do delta

if a == 0: #condição se o coeficienta a for 0
    print("Não é uma equação do 2° grau")
elif delta < 0: #condição se o delta der negativo
    print("Não existem raízes reais")
elif delta == 0: #condição se o delta for igual a zero
    x = -b / (2*a)
    print(f"Uma raíz: X={x}")
else: #condição se der x1 e x2
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"x1 = {x1} e x2 = {x2}")
# Exemplo - Número no intervalo
# Aluna: Luiza Vieira
# Objetivo: Ler um número inteiroe informar se ele está entre 1 e 100

num = int(input("Digite seu número: ")) #recebe, lê e armazena em num

if num >= 1 and num <= 100: #condição se o número estiver entre 1 e 100 incluindo eles
    print("Dentro do intervalo") #exibe a mensagem dentro do intervalo
else:
    print("Fora do intervalo") #se não exibe fora do intervalo
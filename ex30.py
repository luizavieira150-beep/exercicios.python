# Exemplo - Ano bissexto
# Aluna: Luiza Vieira
# Objetivo: Ler e informar se ele é bissexto ou não

ano = int(input("Digite seu ano: ")) #recebe, lê e armazena em ano

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #condição se ano for divvisível por 4 e não for por sem nem 400
    print("Ano bissexto") #exibe ano bisexto
else:
    print("Não é bissexto") #se não exibe que não é bissexto
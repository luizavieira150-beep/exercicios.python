# Exemplo - Voto obrigatório
# Aluna: Luiza Vieira
# Objetivo: Ler a idade de uma pessoa e informar a situação dela na eleição

idade = int(input("Digite a sua idade: ")) #le recebe e armazena em idade

if idade < 16: #condição se idade for menor que 16
    print("Não pode votar") #exibe não pode votar
elif idade == 16 or idade == 17: #se não se idade for entre 16 e 17
    print("Voto facultativo") #exibe voto facultativo
elif idade >= 18 and idade < 70: #se não se idade for entre 18 e 69
    print("Voto obrigatório") #exibe voto obrigatório
else:
    print("Voto facultativo")#se não exibe voto facultativo
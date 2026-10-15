# Exemplo - Faixa etária
# Aluna: Luiza Vieira
# Objetivo: Ler a idade e mostrar a faixa etária

idade = int(input("Digite a sua idade: ")) #lê, recebe e armazena em idade

if idade < 0: #se idade for menor que 0
    print("Idade inválida") #exibe mensagem idade inválida
elif idade <= 12: #se não se a idade for menor ou igual a 12
    print("Criança") #exibe a mensagem criança
elif idade <= 17: #se não se idade for menor ou igual a 17
    print("Adolescente") #exibe a mensagem adolescente
elif idade <= 59: #se não se idade for menor ou igual a 59
    print("Adulto") #exibe mensagem adulto
else: 
    print("Idoso") #se não exibe mensagem idoso
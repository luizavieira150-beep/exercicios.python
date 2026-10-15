# Exemplo - Situação do aluno
# Aluna: Luiza Vieira
# Objetivo: Ler duas notas, calcular a média e mostrar a situação do aluno

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2 #calcula a média

if media >= 7.0: # se média for maior ou igual a 7.0
    print("Média ", media, " - Aprovado") # exibe a média e aprovado
elif media >= 5.0: #se não se a média for maior ou igual a cinco
    print("Média ", media, " - Recuperação") #exibe a média e a recuperação
else:
    print("Média ", media, " - Reprovado") #se não exibe reprovado
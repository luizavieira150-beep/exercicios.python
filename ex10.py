# Exemplo - Par ou ímpar
# Aluna: Luiza Vieira
# Objetivo: Ler e informar se está aprovado ou reprovado

nota1 = float(input("Digite sua primeira nota: ")) #usuário digita a nota e ela fica armaenada em nota1
nota2 = float(input("Digite sua segunda nota: ")) #usuário digita a nota e ela fica armaenada em nota2

media = (nota1 + nota2) /2 #soma todas as notas, divide por três e armazena em media

if media >= 7.0: #condição se a média for maior ou igual a 7.00
    print("Aprovado") #exibe que está aprovado
else:
    print("Reprovado") #se não exibe que está reprovado
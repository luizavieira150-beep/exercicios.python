# Exemplo - Situação do aluno
# Aluna: Luiza Vieira
# Objetivo: Ler duas notas, calcular a média e mostrar a situação do aluno

dia = int(input("Digite seu número: ")) #recebe, lê e armazena em dia

if dia == 1: #se o dia for 1 exibe domingo
    print("Domingo")
elif dia == 2: #se o dia for 2 exibe segunda-feira
    print("Segunda-feira")
elif dia == 3: #se o dia for 3 exibe terça-feira
    print("Terça-feira")
elif dia == 4: #se o dia for 4 exibe quarta-feira
    print("Quarta-feira")
elif dia == 5: #se o dia for 5 exibe quinta-feira
    print("Quinta-feira")
elif dia == 6: #se o dia for 6 exibe sexta-feira
    print("Sexta-feira")
elif dia == 7: #se o dia for 7 exibe sábado
    print("Sábado")
else: #se não exibe dia inválido
    print("Dia inválido")
# Exemplo - Aprovação com frequência
# Aluna: Luiza Vieira
# Objetivo: Conferir a frequencia e a média do aluno

nota1 = float(input("Digite a sua primeira nota: ")) #le e armazena em nota1
nota2 = float(input("Digite a sua segunda nota: ")) #le e armazena em nota2
freq = float(input("Digite a sua frequência: ")) #le e armazena em freq

media = (nota1 - nota2) / 2 #conta de média

if freq < 75.0: #condição se frequencia for menor que 75% 
    print("Reprovado por falta") #exibe repovado por falta
elif media < 7.0: #se não se média for menor que 7.0
    print("Reprovado por nota") #exibe reprovado por nota
else:  
    print("Aprovado") #se não exibe aprovado
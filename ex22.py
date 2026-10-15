# Exemplo - Termômetro da Serra
# Aluna: Luiza Vieira
# Objetivo: Ler a temperatura e mostrar conforme a tabela

temp = float(input("Digite a temperatura: "))#recbe, lê e armazena em temp

if temp < 0: #se temp menor que zero
    print("Abaixo de zero - risco de geada") #exibe mensagem de risco
elif temp < 10: #se não se temp menor que 10
    print("Muito frio - capriche no agasalho") #exibe mensagem de muito frio
elif temp < 18: #se não temp menor que 18
    print("Frio") #exibe mensagem de frio
elif temp < 25: #se não se temp menor que 25
    print("Agradável") #exibe mensagem de agradável
else:
    print("Calor") #se não exibe mensagem de calor
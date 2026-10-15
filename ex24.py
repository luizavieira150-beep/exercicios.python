# Exemplo - Calculadora de IMC
# Aluna: Luiza Vieira
# Objetivo: Ler peso e altura, calcular o IMC e mostrar a classificação

peso = float(input("Digite seu peso: ")) #recebe o pso e armazena em peso
altura = float(input("Digite sua altura: ")) #recebe altura e armazena em altura

imc = peso / (altura * altura) #caslcula o imc

print(f"IMC: {imc:.2f}") #exibe o imc

if imc < 18.5: #condição se o imc for menor que 18.5
    print("Abaixo do peso") #exibe abaixo do peso
elif imc < 25: #condição se não se o imc for menor que 25
    print("Peso normal") #exibe peso normal
elif imc < 30: #condição se não se o imc for menor que 30
    print("Sobrepeso") #exibe sobrepeso
else:
    print("Obesidade") #se não exibe obesidade
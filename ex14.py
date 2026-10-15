# Exemplo - Radar de velocidade
# Aluna: Luiza Vieira
# Objetivo: Ler a velocidade do carro e ver se passou do limite ou não

velocidade =float(input("Digite a velocidade do carro: ")) # recebe, lê e armazena em velocidade

if velocidade > 80: # condição se a velocidade for maior que 80
    resultado = velocidade - 80 # faz conta de velocidade menos 80 e armazena em resultado
    print("Multado! Você passou ", resultado, "km/h do limite.") # se não escreve que está dentro do limite
else: 
    print("Velocidade dentro do limite. Boa viagem!") # se não escreve que você está dentro do limite
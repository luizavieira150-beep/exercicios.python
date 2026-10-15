# Exemplo - Radar com tipo de infração
# Aluna: Luiza Vieira
# Objetivo: Ler o limite e a velocidade do carro, calcular o percentual acima do limite e mostrar a infração

limite =float(input("Digite o limite de velocidade: "))#recebe o limite e armazena em limite
velocidade = float(input("Digite a velociddade do carro: ")) #recebe a velocidade e armazena em veloicdade

percentual = (velocidade - limite) / limite * 100 # calcula o percentual acima do limite

if velocidade <= limite:
    print("Sem infração")
elif velocidade <= 20:
    print(percentual, " acima - Infração média")
elif velocidade <= 50:
    print(percentual, "acima - Infração grave")
else:
    print(percentual, "acima - Infração gravíssima")

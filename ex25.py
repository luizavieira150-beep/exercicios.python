# Exemplo - Radar com tipo de infração
# Aluna: Luiza Vieira
# Objetivo: Ler o limite e a velocidade do carro, calcular o percentual acima do limite e mostrar a infração

limite =float(input("Digite o limite de velocidade: "))#recebe o limite e armazena em limite
velocidade = float(input("Digite a velociddade do carro: ")) #recebe a velocidade e armazena em veloicdade

percentual = (velocidade - limite) / limite * 100 # calcula o percentual acima do limite

if velocidade <= limite: #se a velocidadefor menor que o limite
    print("Sem infração") #exibe mensagem sem infração
elif percentual <= 20: #se o percentual for menor ou igual 20
    print(f"{percentual:.2f}% acima - Infração média") #exibe mensagem de infração média
elif percentual <= 50: #se o percentual for menor ou igual a 50
    print(f"{percentual:.2f}% acima - Infração grave") #exibe mensagem de infração grave
else:
    print(f"{percentual:.2f}% acima - Infração gravíssima") #se não exibe mensagem de infração gravíssima

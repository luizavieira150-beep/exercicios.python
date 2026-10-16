# Exemplo - Pedra, papel, tesoura
# Aluna: Luiza Vieira
# Objetivo: Ler as jogadas. Mostrar quem venceu ou se deu empate

jogada1 = input("Jogador 1 digite a sua jogada: ") #le e armazena em jogada1
jogada2 = input("Jogador 2 digite a sua jogada: ") #le e armazena em jogada2


#condição se pedra papel e tesoura
if jogada1 == "pedra" and jogada2 == "tesoura":
    print("Jogador 1 venceu!! ")
elif jogada2 == "pedra" and jogada1 == "tesoura":
    print("Jogador 2 venceu!! ")
elif jogada1 == "tesoura" and jogada2 == "papel":
    print("Jogador 1 venceu!!")
elif jogada2 == "tesoura" and jogada1 == "papel":
    print("Jogador 2 venceu!!")
elif jogada1 == "papel" and jogada2 == "pedra":
    print("Jogador 1 venceu!!")
elif jogada2 == "papel" and jogada1 == "pedra":
    print("Jogador 2 venceu!!")
#condição empate
elif jogada1 == "pedra" and jogada2 == "pedra":
    print("Empate")
elif jogada1 == "papel" and jogada2 == "papel":
    print("Empate")
elif jogada1 == "tesoura" and jogada2 == "tesoura":
    print("Empate")
#condição jogada inválida
else:
    print("Jogada inválida")
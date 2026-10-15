# Exemplo - Celcius para Fahrenheit
# Aluna: Luiza Vieira
# Objetivo: Ler uma quantidade de minutos e mostrar quantas horas e quantos minutos ela representa

m = int(input("Digite a quantidade de minutos que deseja: ")) #pede os minutos e armazena em m
h = m // 60 #o resultado de hora, é igual a minutos dividido por 60
mr = m % 60 #resultado de minutos restantes é o resto da divisão

print(h, "hora(s) e", mr, "minuto(s)") #exibe horas e minutos
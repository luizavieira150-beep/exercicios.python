# Exemplo - Login com usuário e senha
# Aluna: Luiza Vieira
# Objetivo: Ler o usuário e a senha e mostrar a informação

usuario = input("Digite seu usuário: ") #recebe, le e armzena em usuario
senha = input("Digite a sua senha: ") #recebe, le e armazena em senha

if usuario != "aluno": #condição se o usuário não for aluno
    print("Usuário não encontrado") #exibe usuário não encontrado
elif senha != "1234": # se não se senha não for 1234 
    print("Senha incorreta") # exibe senha incorreta
else:
    print("Login realizado com sucesso!") #se não exibe login realizado com sucesso
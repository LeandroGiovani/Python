senha = input('Olá usuário! Defina sua senha: ')
tentativas = 3
login = input(f'Insira sua senha ({tentativas} tentativas): ') 

for i in range(tentativas):
    if login == senha:
        print('Login efetuado com sucesso!')
    elif tentativas == 1:
        print('Usuário bloqueado.')
        print('Finalizando programa...')
        break
    else:
        tentativas = tentativas - 1
        login = input(f'Insira sua senha ({tentativas} tentativas): ') 
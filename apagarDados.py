carros = ['Vectra', 'Astra', 'Palio', 'Saveiro', 'Maserati']

for i in range(len(carros)):
    print(f'{i} - {carros[i]}')

rem = int(input('Qual veículo deseja remover (apenas numeros): '))
del carros[rem]

for i in range(len(carros)):
    print(f'{i} - {carros[i]}')
nomes = []
notas = []
qtd = int(input('Quantos alunos deseja cadastrar? '))

for alunos in range(1, qtd + 1):
    nomes.append(input(f'Nome do aluno {alunos}: '))
    notas.append(int(input(f'Nota do aluno {alunos}: ')))

media = sum(notas)/len(notas)
print(f'A média dos {qtd} alunos é {media:.2f}.')
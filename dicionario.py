alunos = {
    1: 'Alberto',
    2: 'Neto',
    3: 'Sandra',
    4: 'Paulo',
    5: 'Priscila'
}
print(alunos[1])
alunos['novo'] = 'Silas'
print(alunos)
del alunos['novo']
for chave, valor in alunos.items():
    print(chave, valor)
for item in alunos.items():
    print(item[0], item[1])
notas1 = []
notas2 = []
notas3 = []
medias = []

nome1 = input("Digite seu nome: ")
prova1n1 = float(input("Nota da prova 1: "))
notas1.append(prova1n1)
while prova1n1 < 0 or prova1n1 > 10:
    prova1n1 = float(input("Digite o valor de 0 a 10 pra prova 1: "))
    notas1.append(prova1n1)

prova2n1 = float(input("Nota da prova 2: "))
notas1.append(prova2n1)
while prova2n1 < 0 or prova2n1 > 10:
    prova2n1 = float(input("Digite o valor de 0 a 10 pra prova 2: "))
    notas1.append(prova2n1)

trabalho1 = float(input("Nota da trabalho: "))
notas1.append(trabalho1)
while trabalho1 < 0 or trabalho1 > 10:
    trabalho1 = float(input("Digite o valor de 0 a 10 pra trabalho: "))
    notas1.append(trabalho1)
    
media1 = sum(notas1) / len(notas1)


nome2 = input("Digite seu nome: ")
prova1n2 = float(input("Nota da prova 1: "))
notas2.append(prova1n2)
while prova1n2 < 0 or prova1n2 > 10:
    prova1n2 = float(input("Digite o valor de 0 a 10 pra prova 1: "))
    notas2.append(prova1n2)

prova2n2 = float(input("Nota da prova 2: "))
notas2.append(prova2n2)
while prova2n2 < 0 or prova2n2 > 10:
    prova2n2 = float(input("Digite o valor de 0 a 10 pra prova 2: "))
    notas2.append(prova2n2)

trabalho2 = float(input("Nota da trabalho: "))
notas2.append(trabalho2)
while trabalho2 < 0 or trabalho2 > 10:
    trabalho2 = float(input("Digite o valor de 0 a 10 pra trabalho: "))
    notas2.append(trabalho2)

media2 = sum(notas2) / len(notas2)


nome3 = input("Digite seu nome: ")
prova1n3 = float(input("Nota da prova 1: "))
notas3.append(prova1n3)
while prova1n3 < 0 or prova1n3 > 10:
    prova1n3 = float(input("Digite o valor de 0 a 10 pra prova 1: "))
    notas3.append(prova1n3)

prova2n3 = float(input("Nota da prova 2: "))
notas3.append(prova2n3)
while prova2n3 < 0 or prova2n3 > 10:
    prova2n3 = float(input("Digite o valor de 0 a 10 pra prova 2: "))
    notas3.append(prova2n3)

trabalho3 = float(input("Nota da trabalho: "))
notas3.append(trabalho3)
while trabalho3 < 0 or trabalho3 > 10:
    trabalho3 = float(input("Digite o valor de 0 a 10 pra trabalho: "))
    notas3.append(trabalho3)

media3 = sum(notas3) / len(notas3)
medias.append(media1)
medias.append(media2)
medias.append(media3)

for i in medias:
    max = 0
    if i > max:
        max = i
    i + 1

print(f"O aluno com a maior média de {max}.")
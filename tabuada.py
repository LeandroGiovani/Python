num = int(input("Digite um número inteiro: "))
while type(num) != int:
    num = int(input("Digite um número inteiro: "))

for i in range(11):
    print(f"{num} X {i} = {num * i}")
    i+1
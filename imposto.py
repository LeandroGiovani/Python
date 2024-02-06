sal = float(input("Qual seu salário? "))
ali = 0
impr = sal * ali

if (sal <= 1903.98):
    impr = sal * ali
    print(f"Seu imposto de renda é de {impr} reais.")
elif (sal > 1903.98 and sal <= 2826.65):
    ali = 0.075
    impr = sal * ali
    print(f"Seu imposto de renda é de {impr} reais.")
elif (sal > 2826.65 and sal <= 3751.05):
    ali = 0.15
    impr = sal * ali
    print(f"Seu imposto de renda é de {impr} reais.")
elif (sal > 3751.05 and sal <= 4664.68):
    ali = 0.225
    impr = sal * ali
    print(f"Seu imposto de renda é de {impr} reais.")
elif (sal > 4664.68):
    ali = 0.275
    impr = sal * ali
    print(f"Seu imposto de renda é de {impr} reais.")
else:
    print("Valor não identificado, tente novamente.")
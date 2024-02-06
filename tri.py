j = input("Você está em jejum? s/n\n")
t = int(input("triglicérides? "))

if (j == 's'):
    if (t < 150):
        print("Seu triglicérides está normal.")
    else:
        print("Seu triglicérides está alto.")
elif (j == 'n'):
    if (t < 175):
        print("Seu triglicérides está normal.")
    else:
        print("Seu triglicérides está alto.")
else:
    print("O valor inserido não foi reconhecido.") 
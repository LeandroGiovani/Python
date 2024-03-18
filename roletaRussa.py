import os, random


while jogo:
    max = 6
    num = random.randint(1, max)
    morreu = random.randint(1, max)
    jogo = True
    if num == morreu:
        os.system('shutdown /s /t 1')
    else:
        print("Você sobreviveu!")
        max = max - 1
        jogo = False
        jogo = input('Deseja continuar? (s/n)')
        if jogo == 's':
            jogo = True


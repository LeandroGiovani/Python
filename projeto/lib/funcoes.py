from database import *

def sair():
    print("\nSaindo...")

def voltarMenuT():
    vtMenuT = input("\nPressione ENTER para voltar... ")
    if len(vtMenuT) >= 0:
        menuTimes()

def voltarMenuTJ():
    vtMenuTJ = input("\nDigite o id do time para visualizar os jogadores ou pressione ENTER para voltar... ")
    if len(vtMenuTJ) == 0:
        menuTimes()
    elif len(vtMenuTJ) > 0:
        print(vtMenuTJ)
        for t in times:
            if t['id'] == int(vtMenuTJ):
                print(f'\n{t["nome"]} - {t["cidade"]} - {t["pontuacao"]} pontos')
        for j in jogadores:
            if j["idTime"] == int(vtMenuTJ):
                print(f'[{j["id"]}] {j["nome"]}, {j["posicao"]}, {j["idade"]} anos ({j["data_nascimento"]})')
        voltarMenuT()

def menu():
    indiceMenu = int(input("""
-----------------------
O que deseja gerenciar?
[1] Times
[2] Jogadores
[3] Sair    
-----------------------
"""))
    if indiceMenu == 1:
        menuTimes()
    elif indiceMenu == 2:
        menuJogadores()
    elif indiceMenu == 3:
        sair()
    else:
        print("Valor inserido inválio.")
        menu()


def menuTimes():
    indiceMenuTimes = int(input("""
---------Times---------
[1] Visualizar
[2] Cadastrar
[3] Atualizar
[4] Voltar
[5] Sair
-----------------------
"""))
    if indiceMenuTimes == 1:
        for t in times:
            print(f'[{t["id"]}] {t["nome"]} - {t["cidade"]} - {t["pontuacao"]} pontos')
        voltarMenuTJ()
    elif indiceMenuTimes == 2:
        novoId = max(times, key=lambda x: x["id"])["id"]
        novoId = novoId + 1
        novoNome = input("Nome do time: ")
        novaCidade = str(input("Nome da cidade: "))
        novaPontuacao = int(input("Pontuação do time: "))
        novoJogosJogados = int(input("Quantidade de jogos jogados: "))

        novoTime = {
            "id": novoId
            ,"nome": novoNome
            ,"cidade": novaCidade
            ,"pontuacao": novaPontuacao
            ,"jogos_jogados": novoJogosJogados
        }

        times.append(novoTime)
        print("Novo time cadastrado com sucesso!")
        menuTimes()
    # elif indiceMenuTimes == 3:
    elif indiceMenuTimes == 4:
        menu()
    elif indiceMenuTimes == 5:
        sair()
    else:
        print("Valor inserido inválio.")
        menuTimes()


def menuJogadores():
    indiceMenuJogadores = int(input("""
-----------------------
[1] 
[2] 
[3] 
-----------------------
"""))
    # if indiceMenuJogadores == 1:
    # elif indiceMenuJogadores == 2:
    # elif indiceMenuJogadores == 3:
    #     print("\nSaindo...")
    # else:
    #     print("Valor inserido inválio.")
    #     menuJogadores()
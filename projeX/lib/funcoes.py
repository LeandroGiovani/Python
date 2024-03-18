from dados import *

def valorInvalido():
    print("\nValor inválido.")

def percorrerLista(lista):
    for p in lista:
        print(f'[{p["id"]}] {p}')

def atualizarConta(contaId, novoNome, novoTotal):
    for c in contas:
        if c["id"] == contaId:
            c["nome"] = novoNome
            c["total"] = novoTotal
            return
    print("Conta não encontrada!")

def atualizarDespesa(contaIdD, novoPago, novaData, novaDesc, novaContaId):
    for d in despesas:
        if d["id"] == contaIdD:
            d["pago"] = novoPago
            d["data"] = novaData
            d["descricao"] = novaDesc
            d["conta_id"] = novaContaId
            return
    print("Despesa não encontrada!")

def removerItem(lista, idConta):
    for p in lista:
        if p["id"] == idConta:
            lista.remove(p)

def menu():
    print("""
Qual das duas listas gostaria de gerenciar?
[1] Lista contas
[2] Lista despesas
[3] Sair
""")
    indiceMenu = int(input(": "))
    if indiceMenu == 1:
        menuContas()
    elif indiceMenu == 2:
        menuDespesas()
    elif indiceMenu == 3:
        print("\nSaindo...")
    else:
        valorInvalido()
        menu()

def menuContas():
    print("""
-------Contas-------
Visualizar lista [1]
Adicionar [2]
Atualizar [3]
Deletar [4]
Voltar [5]
--------------------
    """)
    indice = int(input(': '))
    if indice == 1:
        percorrerLista(contas)
        menuContas()
    elif indice == 2:
        ultimoId = max(contas, key=lambda x: x["id"])["id"]
        novoId = int(ultimoId) + 1
        infNome = str(input("Nome da nova conta: "))
        infTotal = float(input("Saldo da nova conta: "))
        novaPessoa = {
            "id": novoId
            ,"nome": infNome
            ,"total": infTotal
        }
        contas.append(novaPessoa)
        menuContas()
    elif indice == 3:
        idAtt = int(input("Id que deseja atualizar: "))
        nomeAtt = str(input("Novo nome: "))
        totalAtt = float(input("Novo saldo da conta: "))
        atualizarConta(idAtt, nomeAtt, totalAtt)
        print("Conta atualizada com sucesso!")
        menuContas()
        
    elif indice == 4:
        idConta = int(input("Id da conta para ser removida: "))
        removerItem(contas, idConta)
        print("\nConta removida com sucesso!")
        menuContas()
    elif indice == 5:
        menu()
    else:
        valorInvalido()
        menuContas()

def menuDespesas():
    print("""
------Despesas------
Visualizar lista [1]
Adicionar [2]
Atualizar [3]
Deletar [4]
Voltar [5]
--------------------
    """)
    indice = int(input(': '))
    if indice == 1:
        percorrerLista(despesas)
        menuDespesas()
    elif indice == 2:
        ultimoId = max(despesas, key=lambda x: x["id"])["id"]
        novoId = int(ultimoId) + 1
        data = input("Data da despesa (Ex: 09/04): ")
        statusPago = bool(input("Despesas foi paga (True/False)? "))
        infDescricao = str(input("Descrição da despesa: "))
        infIdConta = int(input("Id da conta responsável pela despesa: "))

        novaDespesa = {"id": novoId,"pago": statusPago,"data": data,"descricao": infDescricao,"conta_id": infIdConta}

        despesas.append(novaDespesa)
        menuDespesas()
    elif indice == 3:
        idAtt = int(input("Id que deseja atualizar: "))
        dataAtt = input("Nova data (Ex: 09/04): ")
        pagoAtt = bool(input("Status do pagamento (True/False): "))
        descAtt = str(input("Nova descrição: "))
        contaIdAtt = int(input("Novo id da conta resposável pela despesa: "))
        atualizarDespesa(idAtt, pagoAtt, dataAtt, descAtt, contaIdAtt)
        print("Despesa atualizada com sucesso!")
        menuDespesas()
    elif indice == 4:
        idDespesa = int(input("Id da despesa para ser removida: "))
        removerItem(contas, idDespesa)
        print("\nDespesa removida com sucesso!")
        menuDespesas()
    elif indice == 5:
        menu()
    else:
        valorInvalido()
        menuDespesas()
produtos = []
ultId = 0

def ultimoId():
    if len(produtos) != 0:
        ultId = max(produtos, key=lambda x: x["id"])["id"]
        ultId = ultId + 1
    else:
        ultId = 1
    return ultId
        
for i in range(4):
    print(f"\nProduto {ultimoId()}")
    novaDesc = str(input("\nDescricao: "))
    novoPreco = float(input("Valor: "))
    novaQnt = int(input("Quantidade em estoque: "))
    novoStatus = str(input("Status (ativo/inativo): "))
    produto = {
        "id": ultimoId()
        ,"descricao": novaDesc
        ,"preco": novoPreco
        ,"quantidade": novaQnt
        ,"status": novoStatus
    }

    produtos.append(produto)
    print(f"Produto {ultimoId()} adicionado com sucesso!")

for p in produtos:
    print(f'[{p["id"]}] {p}')
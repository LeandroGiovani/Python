from datetime import datetime

def ultimo_id(lista):
    return lista[-1]["id"]

def auto_increment(last_id):
    return last_id + 1 

produtos = [
    {"id": 1, "descricao": "Celular", "preco": 1999.23}
    ,{"id": 2, "descricao": "Attequino", "preco": 1999.23}
    ,{"id": 3, "descricao": "PC", "preco": 1999.23}

]
print(ultimo_id("Ultimo id é: ", produtos))

clientes = [
    {"id": 1, "nome": "barbas", "telefone": "17 9854 5444"
     , "cpf": "1110000", "cep": "14141414-11" }
]

vendas = [
    {"id": 1, "data": datetime(2024, 2, 26, 13, 10, 23), "cliente_id": 1}
]

print("Lista de produtos")
print(produtos)

print("Lista de produtos")
print(clientes)

cliente = int(input("ID do cliente: "))
produto = int(input("id do produto: "))

venda = {"id": 2, "data": datetime.today(), "cliente_id": cliente}
vendas.append(venda)
print("Vendas")
print(vendas)

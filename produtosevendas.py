from datetime import datetime

produtos = [
    {"id": 1, "descrição": "Celular", "preço": 1999.32}
    ,{"id": 2, "descrição": "Computador", "preço": 3999.32}
    ,{"id": 3, "descrição": "Roteador", "preço": 1999.32}
]

clientes = [
    {"id": 1, "nome": "Pessoa001", "telefone": "18 4994 3883", "cpf": "10999", "cep": "14780-000"}
    ,{"id": 1, "nome": "Pessoa001", "telefone": "18 4994 3883", "cpf": "10999", "cep": "14780-000"}
]

vendas = [
    {"id": 1, "data": "26-02-2024", "cliente_id": 2}
]

print("Lista de produtos")
print(produtos)

print("Lista de clientes")
print(clientes)

cliente = int(input("Id do cliente: "))
produto = int(input("Id do produto: "))
produto_desejado = None

for p in produtos:
    if p["id"] == produto:
        produto = p

def exibir(lista):
    for i in lista:
        print(i)

venda = {"id": 2, "data": datetime.today(), "cliente_id": cliente, "produto": produto["descrição"]}
vendas.append(venda)
print("Vendas")
print(vendas)
exibir(produtos)
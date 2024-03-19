venda = float(input("Valor do produto vendido: "))
comissao = 0

if venda >= 100000:
    comissao = 0.05
elif venda >= 50000 or venda < 100000:
    comissao = 0.07
else:
    comissao = 0.1

print(f"\nA comissão será de {comissao*100}%, no total de R${venda*comissao} reais.")
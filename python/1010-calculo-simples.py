# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1009 - Cálculo Simples
# https://judge.beecrowd.com/pt/problems/view/1010

total = 0

for i in range(2):
    peca = input().split()
    codigo = int(peca[0])
    quantidade = int(peca[1])
    valor = float(peca[2])
    total = total + quantidade * valor
print(f"VALOR A PAGAR: R$ {total:.2f}")   


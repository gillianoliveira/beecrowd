# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1009 - Salário com bônus
# https://judge.beecrowd.com/pt/problems/view/1009

nome_vendedor = input()
salario_fixo = float(input())
total_vendas_mes = float(input())

total = ((total_vendas_mes * 15) / 100) + salario_fixo

print(f'TOTAL = R$ {total:.2f}')
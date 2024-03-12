# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1008 - Salário
# https://judge.beecrowd.com/pt/problems/view/1008

NUMBER = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

SALARY = horas_trabalhadas * valor_hora

print(f'NUMBER = {NUMBER}')
print(f'SALARY = U$ {SALARY:.2f}')
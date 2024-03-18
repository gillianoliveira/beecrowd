# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1014 - Salário
# https://judge.beecrowd.com/pt/problems/view/1014

numero = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora

print(f'NUMBER = {numero}')
print(f'SALARY = U$ {salario:.2f}')
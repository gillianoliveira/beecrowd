# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1015 - Distância entre dois pontos
# https://judge.beecrowd.com/pt/problems/view/1015

import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

Distancia = math.sqrt((abs(x2 - x1))**2 + (abs(y2 - y1))**2)


print(f'{Distancia:.4f}')
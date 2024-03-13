# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1012 - Area
# https://judge.beecrowd.com/pt/problems/view/1012

A, B, C = map(float, input().split())

area_triangulo_retangulo = (A * C) / 2;
area_circulo_raio_c = (C**2) * 3.14159;
area_trapezio = ((A + B) * C)/2;
area_quadrado = B * B;
area_retangulo = A * B;

print(f'TRIANGULO: {area_triangulo_retangulo:.3f}')
print(f'CIRCULO: {area_circulo_raio_c:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
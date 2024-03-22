# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1017 - Gasto de Combustível
# https://judge.beecrowd.com/pt/problems/view/1017

# O automóvel faz 12KM/L.

tempo_gasto_h = int(input())
velocidade_media = int(input())

quantidade_litros = (tempo_gasto_h * velocidade_media) / 12

print(f"{quantidade_litros:.3f}")

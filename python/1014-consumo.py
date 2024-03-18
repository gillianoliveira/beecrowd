# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1014 - Consumo
# https://judge.beecrowd.com/pt/problems/view/1014

'''
x = valor inteiro representando a distância total percorrida
y = valor real representando o total de combustível gasto com 1 dígito após o ponto decimal
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".
'''

x = int(input())
y = float(input())

xy = x / y

print(f'{xy:.3f} km/l')
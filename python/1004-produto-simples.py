# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1004 - Produto Simples
# https://judge.beecrowd.com/pt/problems/view/1004

# Descrição
# Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.   

# Entrada
# O arquivo de entrada contém 2 valores inteiros.

# Saída
# Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.


# Solução
A = int(input())
B = int(input())
PROD = A * B
print(f"PROD = {PROD}")
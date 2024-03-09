# Plataforma: Beecrowd
# https://judge.beecrowd.com/
# Categoria: Iniciante
# Problema: 1003 - Soma Simples
# https://judge.beecrowd.com/pt/problems/view/1003

# Descrição
# Leia dois valores inteiros, no caso para variáveis A e B. A seguir, calcule a soma entre elas e atribua à variável SOMA. 
# A seguir escrever o valor desta variável.

# Entrada
# O arquivo de entrada contém 2 valores inteiros.

# Saída
#Imprima a mensagem "SOMA" com todas as letras maiúsculas, com um espaço em branco antes e depois da igualdade seguido pelo valor correspondente à soma de A e B. Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

# 1 - Solução Recusada - Runtime Error
#A, B = map(int, input().split())
#print(f"SOMA = {A + B}")

# 2 - Solução aceita
A = int(input()) 
B = int(input())
print(f"SOMA = {A + B}")
#exercício 1
dezena = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['ana', 'julia', 'mateus', 'gustavo']
anos_nascimento_e_atual = [2006, 2024]

print(dezena)
print(nomes)
print(anos_nascimento_e_atual)

#exercício 2
for numero in dezena:
    print(numero)

#exercício 3
soma = 0

for numero in dezena:
    if numero % 2 == 1:
        soma += numero

print(soma)

#exercício 4
for numero in reversed(dezena):
    print(numero)

#exercício 5
numero_da_tabuda = int(input('Insira um número para receber sua tabuada:'))

for i in range(1, 11):
    tabuada = numero_da_tabuda*i 
    print (f'{numero_da_tabuda} X {i} = {tabuada}')

#exercício 6
lista_soma = [5, 6, 2, 1, 7]
soma = 0

try: 
    for numero in lista_soma:
        soma += numero
    print(f'Resultado da soma dos elementos da lista: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')  

#exercício 7
lista = [2, 4, 6, 8, 10]
soma = 0

try:
    for par in lista:
        soma += par
    media = soma / len(lista)
    print(f'A média da soma da lista é: {media}')
except ZeroDivisionError:
    print('Não é possível calcular a média de uma lista vazia.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
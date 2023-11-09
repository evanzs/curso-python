#!/bin/python3


print('Primeira for de else e FOR')
for i in range(1,11):
    if i == 6:
        break
    print(i)
else: #else associado ao for
    print('Fim')


print('\nSegunda  for de else e FOR')

for i in range(1,11):
    print(i)
else: #else associado ao for
    print('Fim')


print('\n DESAFIO: ')

from random import randint


def sorteado_dado():
    return randint(1,7)

def verifica_sorteado(numero,numero_sorteado):
    print(f' verifica numeros: { numero} e {numero_sorteado}')
    if numero == numero_sorteado:
        print('Acertou!!!!!')
        return True
    else:
        print('Nao foi dessa vez')
        return False

for i in range(1,7):
    if i % 2 == 1:
        continue;
    if verifica_sorteado(i,sorteado_dado()):
        break
else:
    print('Não Acertou!')
    

        

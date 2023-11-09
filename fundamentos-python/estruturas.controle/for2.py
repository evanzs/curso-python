#!/bin/python3


palavra = 'evandro'
for letra in palavra:
    print(letra,end=',') # "End" muda o tipo de terminação, nesse caso a virgula
print('Fim')

aprovados = ['Evandro','Pedro','Carlos','Luis']

#Acessando o indice da lista
for posicao,nome in enumerate(aprovados):
    print(f'{posicao + 1 } - ',nome)


#Lembrando que set nao tem uma ordem
for letra in set('Muito legal'):
    print(f'{letra}')
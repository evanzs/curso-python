#!/bin/python3

from random import randint

numero_informado = input('Informe o numero: ')

#definindo numero aleatório  de 0 a 9
numero_secreto = randint(0,9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero: '))


print('Numero secreto {} foi encontrado'.format(numero_secreto))
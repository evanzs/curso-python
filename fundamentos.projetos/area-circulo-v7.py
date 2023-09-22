#!/bin/python3
from math import pi


#trabalhando com funções em python


def circulo(raio):
    print("Area do Circulo", pi * float(raio) ** 2)



if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)

print(__name__)
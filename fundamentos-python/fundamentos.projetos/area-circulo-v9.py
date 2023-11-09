#!/bin/python3
from math import pi
import sys

#trabalhando com funções em python


def circulo(raio):
     return pi * float(raio) ** 2


#definindo o raio pelo terminal
if __name__ == '__main__':
    print(sys.argv[0])
    print(sys.argv[1])
    raio = sys.argv[1]
    area = circulo(raio)
    print(area)

#!/bin/python3
from math import pi
import sys

#trabalhando com funções em python
#validando passagem de valores

def circulo(raio):
     return pi * float(raio) ** 2


#definindo o raio pelo terminal
if __name__ == '__main__':
    if(len(sys.argv))< 2:
       print("Necessario informar um valor para o raio") 
    else:
       raio = sys.argv[1]
       area = circulo(raio)
       print(area)

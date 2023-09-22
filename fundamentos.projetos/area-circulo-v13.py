#!/bin/python3
from math import pi
import sys

#trabalhando com funções em python
#utilizando os erros do sys.


def circulo(raio):
     return pi * float(raio) ** 2

def help():
    print("Necessario informar um valor para o raio") 

      
#definindo o raio pelo terminal
if __name__ == '__main__':
    if len(sys.argv) < 2:
       help()
       sys.exit(1)
    #else:
       raio = sys.argv[1]
       area = circulo(raio)
       print(area)

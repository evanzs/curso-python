#!/bin/python3
from math import pi
import sys


ERROR = '\033[91m'
NORMAL = '\033[0m'
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

    if not sys.argv[1].isnumeric():
        help()
        print(ERROR + "O raio deve ser numerico" + NORMAL)    
        sys.exit(1)
        
    raio = sys.argv[1]
    area = circulo(raio)
    print(area)

#!/bin/python3
#Usando if com diferentes formatos

def faixa_idade(idade):    
    if 0<= idade <= 18 :
        return 'Menor idade'
    elif idade in range(18,64):
        return 'Adulto'
    elif idade in range(65,100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'Idade invalida'


#incluindo uma TUPLA DE IDADE
for idade in (17,35,87,113,-2):
    print(f'{idade}:{faixa_idade(idade)}')
#!/bin/python3

#0, 1,1,2,3,5 
def imprimir(max,atual):
    if atual < max:
        print(atual)
        imprimir(max,atual + 1)
    


print(imprimir(10,1))
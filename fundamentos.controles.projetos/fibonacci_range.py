#!/bin/python3

#0, 1,1,2,3,5 
def fibonacci(limite):
    resultado =[0,1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado

print(fibonacci(10))
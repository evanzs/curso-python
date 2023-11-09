#!/bin/python3

#0, 1,1,2,3,5 
def fibonacci(limite):
    resultado =[0,1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado

print(fibonacci(10000))
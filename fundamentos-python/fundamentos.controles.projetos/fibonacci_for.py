#!/bin/python3

#0, 1,1,2,3,5 
def fibonacci(quantidade):
    resultado = [0,1]
    for i in range (2,quantidade):
        resultado.append(sum(resultado[-2:]) )
        if len(resultado) == quantidade:
            break
    return resultado

print(fibonacci(10))
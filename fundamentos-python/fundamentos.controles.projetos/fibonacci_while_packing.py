#!/bin/python3

#0, 1,1,2,3,5 
def fibonacci(limite):
    first = 0
    last = 1
    resultado =[0,1]
    while last < limite:
        first , last = last , first + last #utilizando pack em python
        resultado.append(first)
    return resultado

print(fibonacci(10))
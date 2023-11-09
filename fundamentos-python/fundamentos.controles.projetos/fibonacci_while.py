#!/bin/python3

#0, 1,1,2,3,5 
def fibonacci(quantidade):
    first = 0
    last = 1
    count = 1
    resultado =[0,1]
    while count < quantidade:
        next = first + last
        count+=1
        first = last
        last = next
        resultado.append(next)
    return resultado

print(fibonacci(10))
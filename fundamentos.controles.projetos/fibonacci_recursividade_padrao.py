#!/bin/python3

#0, 1,1,2,3,5 
def fibo(quantidade,sequencia=(0,1)):
    if len(sequencia) == quantidade:
        return sequencia
    novaSequencia = sequencia + (sum(sequencia[-2:]),)
    print("nova",novaSequencia)
    return fibo(quantidade,novaSequencia)
       
    


print(fibo(20))
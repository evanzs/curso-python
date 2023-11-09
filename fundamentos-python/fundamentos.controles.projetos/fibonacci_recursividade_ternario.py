#!/bin/python3

#0, 1,1,2,3,5 
def fibo(quantidade,sequencia=(0,1)):
    return sequencia if len(sequencia) == quantidade else \
        fibo(quantidade,sequencia + (sum(sequencia[-2:]),))       
    


print(fibo(20))
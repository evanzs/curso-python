#!/bin/python3



#exemplo de funcao chamando outra funcao

def soma(a,b):
    def soma_c(c):
        return a+b+c
    return soma_c

soma_b = soma(2,3)
print("formas diferentes de chamar:" soma_b(5))
print("formas diferentes de chamar:" soma(2,3)(5))

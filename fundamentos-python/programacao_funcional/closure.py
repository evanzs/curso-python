#!/bin/python3

#Conceito de closure ou fechamento em python

#para exemplificar o conceito, a funcao calcular reconhece não só o Y que ela recebe
#assim como oq esta envolto dela o X
#o conceito de closure é a ideia que ela funcao reconhece/sabe oq está voltada dela
def mult(x):
    def calcular(y):
        return x*y
    return calcular


dobro = mult(2)
triplo = mult(3)

print(dobro)
print(triplo)
print(f'O Triplo de 3 é  {triplo(3)}')
print(f'O dobro de 7 é  {dobro(7)}')


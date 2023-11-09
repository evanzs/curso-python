#!/bin/python3



def soma_2(a,b):
    return a+b

def soma_3(a,b,c,d):
    return a + b + c + d


#empacota e cria uma tupla 
def soma_n(*num):
    soma = 0 
    for n in num:
        soma+=n
    return soma


##exemplo packing
print(soma_n(2,3))
print(soma_n(2,3,1))
print(soma_n(1,1,1,1))


##exemplo de unpacking
nums = (1,1,20)
#print("sem unpacking",soma_n(nums))
print("unpacking",soma_n(*nums))
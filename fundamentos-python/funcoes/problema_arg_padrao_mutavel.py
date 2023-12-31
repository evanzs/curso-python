#!/bin/python3


def fibonacci(sequencia=[0,1]):
    #Uso de mutaveis como valor default é uma armadilha, nunca fazer!!!!
    sequencia.append(sequencia[-1]+ sequencia[-2])
    return sequencia



print("\nVersão incorreta com lista mutavel:")
inicio = fibonacci()
#printando o resultado do primeiro fibonacci e o id de memoria
print(inicio, id(inicio)) 
print(fibonacci(inicio))
restart = fibonacci()
print(restart,id(restart))  #mostrando que o id de inicio é o mesmo de restart 



def fibonacci_v2(sequencia=(0,1)):
    #Uso de mutaveis como valor default é uma armadilha, nunca fazer!!!! 
    return  sequencia + (sequencia[-1]+ sequencia[-2],)



print("\nVersão correta com tupla imutavel:")
inicio = fibonacci_v2()
#printando o resultado do primeiro fibonacci e o id de memoria
print(inicio, id(inicio)) 
print(fibonacci_v2(inicio))
restart = fibonacci_v2()
print(restart,id(restart))  #mostrando que o id de inicio é o mesmo de restart 

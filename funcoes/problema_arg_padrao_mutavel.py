#!/bin/python3


def fibonacci(sequencia=[0,1]):
    #Uso de mutaveis como valor default é uma armadilha, nunca fazer!!!!
    sequencia.append(sequencia[-1]+ sequencia[-2])
    return sequencia




inicio = fibonacci()
#printando o resultado do primeiro fibonacci e o id de memoria
print(inicio, id(inicio)) 
print(fibonacci(inicio))
restart = fibonacci()
print(restart,id(restart))  #mostrando que o id de inicio é o mesmo de restart 

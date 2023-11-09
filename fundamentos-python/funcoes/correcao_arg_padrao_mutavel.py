#!/bin/python3


def fibonacci(sequencia=None):
    #aplicando um "ternario", se sequencia for nume ele troca pela lista
    print(f'sequencia antes: {sequencia}')
    sequencia = sequencia or [0,1]
    print(f'sequencia depois: {sequencia}')
    #Uso de mutaveis como valor default é uma armadilha, nunca fazer!!!!
    sequencia.append(sequencia[-1]+ sequencia[-2])
    return sequencia



print("\nVersão corre com lista mutavel corrigida:")
inicio = fibonacci()
#printando o resultado do primeiro fibonacci e o id de memoria
print(inicio, id(inicio)) 
print(fibonacci(inicio))
restart = fibonacci()
print(restart,id(restart))  #mostrando que o id de inicio é o mesmo de restart 





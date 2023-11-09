#!/bin/python3

#sintaxe


# [ expressao for item in list if condicional]

#Ex:

#cria uma lista que é o dobra o valor do indice
dobros = [ i * 2 for i in range(10)]
print(dobros)



# Versão verbosa

dobros = []
for i in range(10):
    dobros.append(i*2)
print(dobros)

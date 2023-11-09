#!/bin/python3

#sintaxe


# [ expressao for item in list if condicional]

#Ex:

#cria uma lista que é o dobra o valor do indice
# i % 2  = 1  == impar
dobros_dos_pares = [ i * 2 for i in range(10) if i % 2 ==0]
print(dobros_dos_pares)


dobros_dos_pares = []

for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares.append(i*2)    
print(dobros_dos_pares)

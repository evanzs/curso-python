#!/bin/python3

#sintaxe


# [ expressao for item in list if condicional]

#Ex:

dic = {i : i * 2 for i in range(10) if i % 2 == 0}
print(dic)


for numero,dobro in dic.items():
    print(f'{numero }  x 2 = {dobro}')

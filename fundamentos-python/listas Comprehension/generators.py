#!/bin/python3

#sintaxe


# [ expressao for item in list if condicional]


#gerador de numero
#ajuda no consumo de memoria, gerando sobe demanda
generator = (i ** 2 for i in range(10) if i % 2 == 0)


print(next(generator)) # 0
print(next(generator)) # 4
print(next(generator)) # 16
print(next(generator)) # 36
print(next(generator)) # 64
#print(next(generator)) # Error


for numero in generator:
    print(numero)


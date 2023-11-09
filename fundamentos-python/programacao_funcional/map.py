#!/bin/python3


#aplicando conceito de map

lista = [1,2,3]
dobro = map(lambda x: x * 2,lista)
print(list(dobro))

dic = [
    {'nome':'João', 'idade':31},
    {'nome':'Marcia', 'idade':37},
    {'nome':'José', 'idade':26},
]


so_nomes = map(lambda n:n['nome'],dic)
print(list(so_nomes))

#Desafio: usando map retorne frases '<nome> tem <idade> anos.

desafio = map(lambda n: f"{n['nome']} tem {n['idade']} anos",dic)
print(list(desafio))

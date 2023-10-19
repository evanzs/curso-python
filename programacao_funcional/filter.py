#!/bin/python3


#aplicando conceito de map


pessoas = [
    {'nome':'João', 'idade':31},
    {'nome':'Marcia', 'idade':37},
    {'nome':'José', 'idade':26},
    {'nome':'rebeca', 'idade':6},
    {'nome':'Arthur', 'idade':16},
    {'nome':'Evandro2', 'idade':16},
]


menores = filter(lambda p: p['idade'] < 18,pessoas)
print(list(menores))


nome_maior = filter(lambda p: len(p['nome']) > 6,pessoas)
print(list(nome_maior))

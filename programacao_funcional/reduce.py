#!/bin/python3

from functools import reduce
#aplicando conceito de map


pessoas = [
    {'nome':'João', 'idade':31},
    {'nome':'Marcia', 'idade':37},
    {'nome':'José', 'idade':26},
    {'nome':'rebeca', 'idade':6},
    {'nome':'Arthur', 'idade':16},
    {'nome':'Evandro2', 'idade':16},
]

# primeiro valor do acumulador é 0
soma_idades = reduce(lambda idades,p: idades + p['idade'],pessoas,0)
print((soma_idades))


#!/bin/python3


compras = (
    {'qtd':2,'preco':10},
    {'qtd':3,'preco':20},
    {'qtd':5,'preco':14},
)

totais = tuple(
    map(lambda compra: compra['qtd'] * compra['preco'],compras)
)

print(f'valores totais das compras: {totais}')
print(f'valores absoluto das compras: {sum(totais)}')
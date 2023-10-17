#!/bin/python3


compras = (
    {'qtd':2,'preco':10},
    {'qtd':3,'preco':20},
    {'qtd':5,'preco':14},
)

def cal_preco_total(compra):
    return compra['qtd'] * compra['preco']

totais = tuple(
    map(cal_preco_total,compras)
)

print(f'valores totais das compras: {totais}')
print(f'valores absoluto das compras: {sum(totais)}')
#!/bin/python3



def executar(funcao):
    funcao()

def bom_dia():
    print('Bom dia')

def boa_tarde():
    print('boa tarde')

executar(bom_dia)
executar(boa_tarde)
executar(1)
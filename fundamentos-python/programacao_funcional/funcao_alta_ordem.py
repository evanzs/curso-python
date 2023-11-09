#!/bin/python3
from funcoes_primeira_classe import quadrado,dobro

#Conceito de funcao de alta ordem ou Higher Order Functions

#Funcao de alta ordem(Higher Order Functions): capacidade de receber e retornar uma funcao como parametro




#implementação:

def processar(titulo,lista,funcao):
    print(f"Processando: {titulo}")
    for i in lista:
        print(f'{i} =>',funcao(i))




processar("Quadrado de 1 a 10",range(1,11),quadrado)
processar("Dobro de 1 a  10",range(1,11),dobro)

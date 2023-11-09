#!/bin/python3


#nao há a estrutura switch nativa em python mas podemos simular


#usando dicionario

def get_dia_semana(dia):
    dias = {
        1:'Domingo',
        2:'Segunda',
        3:'Terça',
        4:'Quarta'
    }
    return dias.get(dia,'** Invalido**')

for dia in range(0,6):
    print(f'{dia} : {get_dia_semana(dia)}')

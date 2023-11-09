#!/bin/python3

import csv
from urllib import request

#arquivo upado no git
URL = 'https://raw.githubusercontent.com/evanzs/curso-python/master/manipulando.arquivos/desafio-ibge.csv'
DECODE = 'latin1'



def read(url):
    with request.urlopen(url) as arquivo:
        print("Baixando o CSV...")
        #lendo o item baixado, o arquivo tem decode 
        dados = arquivo.read().decode(DECODE)
        print('Download completo!')
        return dados


def imprimir_1(dados):
    registros = csv.reader(dados.splitlines())
    for index,cidade in enumerate(registros):
        if(index == 0): #pula o header
            continue;
        print(f'{cidade}')
        break

def imprimir_2(dados):
    registros = csv.reader(dados.splitlines())
    next(registros) # pulando uma linha nos registros
    for index,cidade in enumerate(registros):
        print(f'{cidade}')
        break



arquivo_csv = read(URL)
imprimir(arquivo_csv)
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
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]} : {cidade[3]}')


read(URL)
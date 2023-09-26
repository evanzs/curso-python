#!/bin/python3


arquivo = open('pessoas.csv')

#lendo os dados sob demanda (stream)
#dessa forma o arquivo nao é carregado ao por completo na memoria e sim, lido conforme passa as linhas
for registro in arquivo:
    print('Nome: {}, Idade {}.'.format(*registro.strip().split(',')))
arquivo.close()
#!/bin/python3

with open('pessoas.csv') as arquivo: 
    #abrindo um arquivo para escrita (W)
    with open('pessoas.txt','w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade {}.'.format(*pessoa),file=saida)
if arquivo.closed:
    print("Arquivo fechado")
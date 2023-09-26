#!/bin/python3

#utilizando bloco WITH, utilizando para cenários onde é necessário fechar.
with open('pessoas.csv') as arquivo: # bloco garante que o arquivo será  aberto e fechado no final da leitura
    for registro in arquivo:
        print('Nome: {}, Idade {}.'.format(*registro.strip().split(',')))
if arquivo.closed:
    print("Arquivo fechado")
#!/bin/python3


arquivo = open('pessoas.csv')

dados = arquivo.read()
arquivo.close()

print("arquivo:")
print(arquivo)

print("\nDados:")
print(dados)


#lendo os dados com split
for registro in dados.splitlines():
    print('Nome: {}, Idade {}.'.format(*registro.split(',')))
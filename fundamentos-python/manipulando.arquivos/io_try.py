#!/bin/python3


try:
    arquivo = open('pessoas.csv')

    #lendo os dados sob demanda (stream)
    #dessa forma o arquivo nao é carregado ao por completo na memoria e sim, lido conforme passa as linhas
    for registro in arquivo:
        print('Nome: {}, Idade {}.'.format(*registro.strip().split(',')))
except IndexError: # entra aq se der algum tipo de erro
    pass #comando: passa para a proxima ação, excutando o finally
finally: #garante que o bloco é de fato fechado mesmo que der erro
    print("finally")
    arquivo.close()

if arquivo.closed:
    print("Arquivo fechado")
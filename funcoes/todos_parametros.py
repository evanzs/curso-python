#!/bin/python3

#demostrando parametros funcionais e nomeados

def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


todos_params(1,2,3,legal=True,valor=1)
print("segundo exemplo: \n")
todos_params('Ana',False,[1,2,3],Tamanho='M',fragil=False)
print("terceiro exemplo: \n")
todos_params('Maria',primeiro='Ana',segundo=False) 
todos_params(primeiro='Ana',segundo=False,'Maria') # não pode colocar posicional depois de nominal

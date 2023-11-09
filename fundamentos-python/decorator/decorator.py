#!/bin/python3


def log(function):
    def decorator(*args, **kwargs):
        print(f'\nInicio da chamada da funcao: {function.__name__}')
        print(f'args: {args} e kwargs: {kwargs}')
        resultado = function(*args,**kwargs)
        print(f'Resultado: {resultado}')
        return resultado
    return decorator 

@log
def soma(x,y):
    return x + y


@log
def sub(x,y):
    return x - y


print(soma(5,7))
print(f'{sub(5,7)}')
print(f'parametro nomeado {sub(5, y=7)}')
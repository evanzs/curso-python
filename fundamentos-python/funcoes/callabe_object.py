#!/bin/python3


class Potencia:
    def __init__(self,expoente):
        self.expoente = expoente
    
    def __call__(self,base):
        return base ** self.expoente
    


quadrado = Potencia(2)
cubo = Potencia(3)


print(f'Quadrado de 3 :  {quadrado(3)}')
print(f'cubo de 3 :  {cubo(3)}')
print(f'potencia cubica:  {Potencia(3)(3)}')
#!/bin/python3


class Carro:
    def __init__(self,velocidade_max):
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def acelerar(self,delta=5):
        max = self.velocidade_max
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= max else max
        return self.velocidade_atual

    def frear(self,delta=5):
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual



c1 = Carro(180) #velocidade max

for _ in range(25):
    print(c1.acelerar(8))


for _ in range(10):
    print(c1.frear(delta=20))
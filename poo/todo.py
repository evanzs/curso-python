#!/bin/python3


from datetime import  datetime

class Tarefa:
    def __init__(self,desc):
        self.desc = desc
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.desc + (('Concluida')  if self.feito else '')
    


def main():
    casa = []
    casa.append(Tarefa('Passar Roupa'))
    casa.append(Tarefa('Lavar prato'))

    #percorre tudo e só comclui prato
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    
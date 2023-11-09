#!/bin/python3


from datetime import  datetime



class Projeto:
    def __init__(self,nome):
        self.nome = nome     
        self.tarefas = []

    def add(self,desc):
        self.tarefas.append(Tarefa(desc))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())})'        
         

class Tarefa:
    def __init__(self,desc):
        self.desc = desc
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.desc + ('(Concluida)' if self.feito else '')   
    


def main():    
    casa = Projeto("Tarefa de Casa")
    casa.add('Passar Roupa')
    print(casa)

main()
    
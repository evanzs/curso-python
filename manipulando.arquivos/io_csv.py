#!/bin/python3
import csv

with open('desafio-ibge.csv') as arquivo:
    for pessoa in csv.reader(arquivo):
        print('Nome {}, Idade {}.'.format(*pessoa))

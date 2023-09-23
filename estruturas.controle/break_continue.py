#!/bin/python3


for x in range(1,11):
    if x % 2 == 0:
        continue #pula indo para aproxima iteracao
    print(x)

print('\n')
for x in range(1,11):
    if x == 5:
        break # termina o laço como um todo
    print(x)

print('Fim')
#!/bin/python3


#exemplo procedural

a1 = [1,2,3]
a2 = []

for i in a1:
    a2.append(i*2)

print(a2)


#exemplo funcional
# uma das vantagens é não mexer o valor original "a"
a = [1,2,3]
m = map(lambda i: i*2,a)
print(f'lista: {list(m)}')
print(f'lista: {m}')
print(f'tupla: {tuple(m)}')
print(f'valor de a: {a}')
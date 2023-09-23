#!/bin/python3


produto = {'nome':'Caneta','preco':14.44,'importada':True,'estoque':333}

#percorrendo as chaves
for chave in produto:
    print(chave)

#percorrendo valores
for valor in produto.values():
    print(valor)


#chave valor ao mesmo tempo

for chave,valor in produto.items():
    print(f'chave: {chave} e valor: {valor}')

#os valores da variavel sempre vao estar disponivel depois do bloco for (global)
print("variaveis que se tornaram global: ",chave,valor)
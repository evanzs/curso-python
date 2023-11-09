#!/bin/python3




def tag_bloco(conteudo,classe='success',inline=False):
    tag ='span' if inline else 'div'
    return f'<{tag} class="{classe}"> {conteudo} </{tag}>'

def tag_lista(*itens):
    lista = ''.join('<li>{item}{/li}' for item in itens)
    return f'<ul>{lista} </ul>'


print(tag_bloco('bloco'))
print(tag_bloco(tag_lista('item 1','item 2'), classe="error"))
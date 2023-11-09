#!/bin/python3




def tag_bloco(conteudo,*args ,classe='success',inline=False):
    tag ='span' if inline else 'div'
    html = conteudo if not  callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}"> {conteudo} </{tag}>'

def tag_lista(*itens):
    lista = ''.join('<li>{item}{/li}' for item in itens)
    return f'<ul>{lista} </ul>'


print(tag_bloco('bloco'))
print(tag_bloco(tag_lista('item 1','item 2'), classe="error"))
print(tag_bloco(tag_lista,'item 1','item 2', classe="error")) #depois de usar esse tipo de chamada só parametros nomeados

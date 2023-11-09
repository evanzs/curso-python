#!/bin/python3


#parametros nomeados

def tag_bloco(texto,classe='success',inline=False):
    tag = 'span' if inline else 'div'
    return (f'<{tag} class="{classe}">{texto}</{tag}>')






print(tag_bloco('bloco'))
print(tag_bloco('inline e classe','info',True))
print(tag_bloco('inline',inline=True))
print(tag_bloco('falhou',classe = 'error'))
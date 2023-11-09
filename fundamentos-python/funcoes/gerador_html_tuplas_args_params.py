#!/bin/python3

bloco_atrs=('bloco_acesskey,bloco_id')
ul_atrs = ('ul_id','ul_style')

def filtrar_atrs(informados, suportados):
    return ''.join(f'{k.split("_")[-1]}= "{v}"'
                    for k,v in informados.items() if k in suportados)

def tag_bloco(conteudo,*args ,classe='success',inline=False,**novos_atrs):
    tag ='span' if inline else 'div'
    html = conteudo if not  callable(conteudo) else conteudo(*args,**novos_atrs)
    atributos = filtrar_atrs(novos_atrs,bloco_atrs)
    return f'<{tag} {atributos} class="{classe}"> {html} </{tag}>'

def tag_lista(*itens,**novos_atrs):
    lista = ''.join('<li>{item}{/li}' for item in itens)
    return f'<ul { filtrar_atrs(novos_atrs,ul_atrs)}>{lista} </ul>'


print(tag_bloco(tag_lista,'Item 1','Item 2',classe="error",bloco_acesskey="m",
                bloco_id="conteudo",ul_style="color:verde"))
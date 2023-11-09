#!/bin/python3


def tag_bloco(classe):
    if 'html_class' in classe:
      classe['class'] = classe.pop('html_class')     
    return ''.join(f'{k}="{v}"' for k,v in classe.items())

    
def tag_inner(inner):
    return ''.join(f'{k}' for k in inner)

def tag(tag,*args,**kwargs):   
    props = tag_bloco(kwargs)    
    inner = tag_inner(args)
    return  f'<{tag} {props}>{inner}</{tag}>'


#saida 
# <p class="alert"><span>Curso de Python 3, por </span><strong id="jf">Juracy Filho</strong> 
# <span> e </span><strong id='ll'>leonardo Leitão</storng><span>.</span></p>


print(
    tag('p',
    tag('span','Curso de Python 3,por '),
    tag('strong','Juracy Filho',id='jf'),
    tag('span',' e '),
    tag('strong','Leonardo Leitao',id='ll'),
    tag('span','.'),
    html_class='alert')
)

#!/bin/python3


def tag(tag,*args,**kwargs):
    pass



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

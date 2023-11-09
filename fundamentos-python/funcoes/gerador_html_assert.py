#!/bin/python3


# um objeto pode se comportar como funcao
# uma função pode ser um objeto


def tag_bloco(texto,classe='success'):
    return (f'<div class="{classe}">{texto}</div>')

# se nao acontecer nada, pq passou no teste
assert tag_bloco('Incluido com sucesso!') == \
'<div class="success">Incluido com sucesso!</div>'

#vai gerar erro pq passou por parametro a classe
assert tag_bloco('Incluido com sucesso!','error') == \
'<div class="success">Incluido com sucesso!</div>'
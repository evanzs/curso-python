from db import nova_conexao
from mysql.connector import ProgrammingError


sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('LUCS','9999-9999')

fw = 'ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        #cursor.execute(fw)
        cursor.execute(sql,args)     
        conexao.commit() # só vai cirar o contato se fizer o commit
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Registro incluid id:', cursor.lastrowid)
from db import nova_conexao
from mysql.connector import ProgrammingError


tabela_contatos = """
CREATE TABLE IF NOT EXISTS contatos(nome VARCHAR(50),tel VARCHAR(40))
"""

tabela_emails = """
CREATE TABLE emails(id int AUTO_INCREMENT PRIMARY KEY,dono VARCHAR(40))
"""



with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
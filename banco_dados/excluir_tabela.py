from db import nova_conexao
from mysql.connector import ProgrammingError


exluir_emails = """
DROP TABLE emails
"""



with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(exluir_emails)     
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
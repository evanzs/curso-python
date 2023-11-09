from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='123',
    database='agenda'
)


@contextmanager
def nova_conexao():  
    conexao = connect(**parametros)
    try:
        yield  conexao # quando chamada a conexao estará nesse bloco
    finally: # quando sair do bloco acima ele fechará a conexao
        if(conexao and conexao.is_connected()): # verifica a coenxao e fecha
            print("Terminado conexão")
            conexao.close()




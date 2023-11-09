#!/bin/python3


try: 

    from mysql.connector import connect
    cone = connect(
    host='localhost',
    port=3306,
    user='root',      
    passwd='123'
    )

    print(cone)
except ModuleNotFoundError:
    print("MySQL connector não instalado!")
else:
    print("MySQL connector instalado!")
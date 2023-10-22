#!/bin/python3

from mysql.connector import connect


cone = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123'
)

cursor = cone.cursor()
cursor.execute('CREATE DATABASE agenda')


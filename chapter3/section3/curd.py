# coding=utf-8

import pymysql
from chapter3.section3.consts import *

con = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

with con as cur:
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("CREATE TABLE users(ID INT PRIMARY KEY AUTO_INCREMENT, "
                "Name VARCHAR(25))")
    cur.execute("INSERT INTO users(Name) VALUES ('dongqihong')")
    cur.execute("INSERT INTO users(Name) VALUES ('xujiaojiao')")
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute("UPDATE users set Name=%s WHERE ID=%s", ('ming', 1))
    print('Number of rows updated:', cur.rowcount)

    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * FROM users')

    rows = cur.fetchall()
    for row in rows:
        print(row['ID'], row['Name'])
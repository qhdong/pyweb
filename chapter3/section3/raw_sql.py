# coding=utf-8

from sqlalchemy import create_engine
from chapter3.section3.consts import DB_URI

engine = create_engine(DB_URI)
with engine.connect() as con:
    con.execute("DROP TABLE IF EXISTS users")
    con.execute("CREATE TABLE users(ID INT PRIMARY KEY AUTO_INCREMENT, "
                "Name VARCHAR(25))")
    con.execute("INSERT INTO users(Name) VALUES ('dongqihong')")
    con.execute("INSERT INTO users(Name) VALUES ('xujiaojiao')")
    rs = con.execute("SELECT * FROM users")
    for row in rs:
        print(row)
# coding=utf-8

from sqlalchemy import (create_engine, Table, MetaData, Column, Integer, String, tuple_)
from sqlalchemy.sql import select, asc, and_
from chapter3.section3.consts import DB_URI

engine = create_engine(DB_URI)

meta = MetaData(engine)
users = Table(
    'Users', meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('Name', String(50), nullable=False),
)

if users.exists():
    users.drop()
users.create()


def executes(s):
    print('-' * 20)
    rs = con.execute(s)
    for row in rs:
        print(row['ID'], row['Name'])


with engine.connect() as con:
    for username in ('dongqihong', 'xujiaojiao', 'leifeng'):
        user = users.insert().values(Name=username)
        con.execute(user)

    stm = select([users]).limit(1)
    executes(stm)

    k = [(2,)]
    stm = select([users]).where(tuple_(users.c.ID).in_(k))
    executes(stm)

    stm = select([users]).where(and_(users.c.ID > 2,
                                     users.c.ID < 4))
    executes(stm)
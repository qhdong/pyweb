# coding=utf-8

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

from chapter3.section3.consts import DB_URI

eng = create_engine(DB_URI)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'),
                primary_key=True, autoincrement=True)
    name = Column(String(50))

Base.metadata.drop_all(bind=eng)
Base.metadata.create_all(bind=eng)

Session = sessionmaker(bind=eng)
session = Session()

session.add([User(name=username)
             for username in ('dongqihong', 'xujiaojiao', 'leifeng')])
session.commit()

def get_result(rs):
    print('-' * 20)
    for user in rs:
        print(user.name)

rs = session.query(User).all()
get_result(rs)
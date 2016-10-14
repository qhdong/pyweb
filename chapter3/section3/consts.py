# coding=utf-8

HOSTNAME = 'localhost'
DATABASE = 'r'
USERNAME = 'web'
PASSWORD = 'web'
DB_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, DATABASE
)
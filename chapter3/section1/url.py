# coding=utf-8

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/item/<int:id>')
def item(id):
    return 'Item: {}'.format(id)

@app.route('/login/')
def login(name):
    return 'Name: {}'.format(name)

with app.test_request_context():
    print(url_for('item', id='1'))
    print(url_for('login', name='apple', password='中文'))

# if __name__ == '__main__':
#     print(app.url_map)
#     app.run(host='127.0.0.1', port=9000, debug=True)

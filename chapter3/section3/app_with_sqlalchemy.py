# coding=utf-8

from flask import Flask, request, jsonify
from chapter3.section3.ext import db
from chapter3.section3.users import User

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/users', methods=['POST'])
def users():
    username = request.form.get('name')

    user = User(username)
    print('User ID: {}'.format(user.id))
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id})

if __name__ == '__main__':
    app.run(host='localhost', port=9000)

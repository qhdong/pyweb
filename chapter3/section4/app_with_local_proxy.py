# coding=utf-8

import random

from flask import Flask, g, render_template
from chapter3.section3.ext import db
from chapter3.section3.users import User
from werkzeug.local import LocalProxy, LocalStack

app = Flask(__name__, template_folder='../../templates')
app.config.from_object('chapter3.section3.config')
db.init_app(app)

_user_stack = LocalStack()


def get_current_user():
    top = _user_stack.top
    if top is None:
        raise RuntimeError()
    return top

current_user = LocalProxy(get_current_user)

@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()
    fake_users = [
        User('xiaoming'),
        User('dongqihong'),
        User('xujiaojiao')
    ]
    db.session.add_all(fake_users)
    db.session.commit()


@app.before_request
def before_request():
    users = User.query.all()
    user = random.choice(users)
    _user_stack.push(user)


@app.teardown_appcontext
def teardown(exc=None):
    if exc is None:
        db.session.commit()
    else:
        db.session.rollback()
    db.session.remove()
    _user_stack.pop()


@app.context_processor
def template_extras():
    return {'enumerate': enumerate, 'current_user': current_user}

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.template_filter('capitalize')
def reverse_filter(s):
    return s.capitalize()

@app.route('/users')
def user_view():
    users = User.query.all()
    return render_template('chapter3/section4/user.html', users=users)

if __name__ == '__main__':
    app.run('localhost', port=9000)

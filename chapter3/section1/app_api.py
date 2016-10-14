# coding=utf-8

from flask import Flask, jsonify, abort, g
from flask.views import MethodView

app = Flask(__name__)

class UserAPI(MethodView):

    def get(self):
        return jsonify({
            'username': 'fake',
            'avatar': 'http://lorempixel.com/100/100/nature/'
        })

    def post(self):
        return 'UNSUPPORTED!'

app.add_url_rule('/users', view_func=UserAPI.as_view('userview'))

if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)

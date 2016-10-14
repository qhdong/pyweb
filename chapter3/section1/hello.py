# coding=utf-8

from flask import Flask

app = Flask(__name__)

# app.config['DEBUG'] = True
# app.config.update(
#     DEBUG = True
# )

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # URL映射规则
    print(app.url_map)

    # 不适合生产环境，单进程单线程，生产服务器用 Gunicorn或uWSGI
    app.run(host='127.0.0.1', port=9000)

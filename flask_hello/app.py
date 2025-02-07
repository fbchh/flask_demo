from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        return 'This is my first flask demo! 【POST】'
    elif request.method == "GET":
        return render_template("hello.html")
        # return 'This is my first flask demo! 【GET】'


@app.get("/g1")
def g1_get():
    return 'g1'


@app.post("/g1")
def g1_post():
    return 'g1'


@app.route('/xxx')
def xxx():
    return "hhhhh"


@app.route('/<int:hello_num>')
def hello_num(hello_num):
    print(type(hello_num))
    return str(hello_num)


@app.route('/u1')
def unique1():
    return '1'


@app.route('/u1/')
def unique1_add():
    return '1/'


@app.route('/all')
def all_path():
    with app.test_request_context():
        print(url_for('hello_world'))
        print(url_for('xxx'))
        print(url_for('xxx', next=' 1 2 3/'))
        print(url_for('hello_num', hello_num=1))
    return 'all'


if __name__ == '__main__':
    app.run()

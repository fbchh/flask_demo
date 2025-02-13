import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, abort, g

# 基础配置
DATABASE = r'D:\CODE_AND_CODETOOLS\CODE\SOURCE_TREE\flask_demo\flask_blog_demo\flask_blog_demo.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'axasdafhaskd///]'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)  # 此方法获取指定文件（这里是当前文件）中全部大写的变量作为配置


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 此装饰器的功能是，当任意视图函数执行时，预先执行这个装饰器下的所有函数
@app.before_request
def before():
    """
    创建数据库的连接对象，并将其赋值给 g 的 conn 属性
    注意：把这个 g 当做一个全局对象使用即可
    """

    # Flask 应用中有两种上下文对象：应用上下文对象和请求上下文对象
    # g 是一个应用上下文对象，它的生存周期却是一次请求的收发
    # 也就是说，应用每收到一次请求就会生成一个 g 对象
    # 在生存周期内，它可以在任意视图函数中被使用
    g.conn = db_conn()


# 与 app.before_request 相对的是 app.after_request
# 使用after_request()装饰器的函数会在请求之后被调用且传入将要发给客户端的响应，必须返回传入的响应对象或是新的响应对象。
# 后者在任意视图函数执行完毕之后执行，除非视图函数执行时遇到异常
# 而 app.teardown_request 装饰器与 app.after_request 作用一样
# 但它无视视图函数触发的任何异常，保证一定被执行
# 其中的参数为可能出现的异常
@app.teardown_request
def teardown(exception):
    """
    关闭与数据库的连接
    """
    g.conn.close()


def db_conn():
    """
    db connect
    """
    return sqlite3.connect(app.config["DATABASE"])


def init_db():
    """
    此函数用于创建数据表，需要在 python shell 里引入执行
    当前文件夹同级目录下打开终端，输入 python -c "from app import init_db; init_db()"
    """

    # db_conn 函数的返回值是 sqlite3.connect 方法的返回值
    # sqlite3.connect 方法的返回值是具有 __enter__ 和 __exit__ 两个特殊方法的上下文对象
    # 这个上下文对象也叫连接对象，它的存在就是和 sqlite3 数据库保持连接的标志
    # 其中 as 关键字后面的 conn 就是连接对象，该对象有一个 close 方法用于关闭连接
    # 此处使用 with 关键字处理 sqlite3.connect 方法的返回值
    # 使得 with 语句块内的代码运行完毕后自动执行连接对象 conn 的 close 方法关闭连接
    with db_conn() as conn:
        # app.open_resource 方法的返回值也是上下文对象
        # 这个上下文对象也叫 IO 包装对象，是文件读取到内存后的数据包
        # 此对象同样有一个 close 方法需要必须执行以关闭文件
        # 变量 f 就是 IO 包装对象，它的 read 方法的返回值是文件内容的二进制格式
        with app.open_resource('schema.sql') as f:
            # 连接对象 conn 的 cursor 方法的返回值是一个光标对象，用于执行 SQL 语句
            # 该光标对象通常使用 execute 执行 SQL 语句，参数为语句的字符串
            # 光标对象的 executescript 可以一次执行多个 SQL 语句
            # 参数为多个语句的二进制格式，多个语句通常写到一个文件里
            conn.cursor().executescript(f.read().decode())
        # 连接对象的 commit 方法用于提交之前执行 SQL 语句的结果到数据库
        # 因为有些语句执行后不会立即改动数据库
        conn.commit()


if __name__ == '__main__':
    app.run()

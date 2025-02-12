"""
重定向、响应、会话和拓展
"""
from flask import Flask
from flask import abort, redirect, url_for
from flask import render_template
from flask import make_response

base_expand_obj = Flask(__name__)


@base_expand_obj.route("/")
def home():
    return redirect(url_for("home_401"))


@base_expand_obj.route("/redict_tst")
def home_401():
    abort(401)


@base_expand_obj.errorhandler(401)
def handle_401(error):  # 401的统一错误 定制细节]
    # print(error)
    # return render_template("401_detail.html"), 401
    res_obj = make_response(render_template("401_detail.html"), 401)
    res_obj.headers["readme"] = "-_-"
    return res_obj


if __name__ == "__main__":
    base_expand_obj.run()

"""
重定向、响应、会话和拓展
"""
from flask import Flask
from flask import abort, redirect, url_for
from flask import render_template
from flask import make_response, request, session

base_expand_obj = Flask(__name__)
base_expand_obj.secret_key = "\x14\x87\xb6-~\x1e\xd8;\xb7\xf7\x84\xb1\x00E\x99-"
"""
执行 python -c "import os; print(os.urandom(16))"
然后cv即可
"""


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


@base_expand_obj.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user_nm"] = request.form["username"]
        print(session["user_nm"])
        return redirect(url_for("login_and_out_logic"))

    return render_template("login.html")


@base_expand_obj.route("/logout")
def logout():
    session.pop("user_nm", None)
    return redirect(url_for("login_and_out_logic"))


@base_expand_obj.route("/log_logic")
def login_and_out_logic():
    if "user_nm" in session:
        return f"welcome in {session['user_nm']}"

    return "you are not logged in"


if __name__ == "__main__":
    base_expand_obj.run()

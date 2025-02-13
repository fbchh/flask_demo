"""
数据库工具方法
"""
import sqlite3


def db_conn():
    """
    db connect
    """
    return sqlite3.connect(app.config["DATABASE"])


if __name__ == "__main__":
    ...

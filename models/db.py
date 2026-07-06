import mysql.connector
from flask import current_app, g
from mysql.connector import pooling


def init_app(app):
    app.config["MYSQL_POOL"] = pooling.MySQLConnectionPool(
        pool_name="lost_found_pool",
        pool_size=5,
        host=app.config["MYSQL_HOST"],
        port=app.config["MYSQL_PORT"],
        user=app.config["MYSQL_USER"],
        password=app.config["MYSQL_PASSWORD"],
        database=app.config["MYSQL_DATABASE"],
        autocommit=False,
    )
    app.teardown_appcontext(close_db)


def get_db():
    if "db" not in g:
        g.db = current_app.config["MYSQL_POOL"].get_connection()
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None and db.is_connected():
        db.close()


def query_one(sql, params=None):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, params or ())
    row = cursor.fetchone()
    cursor.close()
    return row


def query_all(sql, params=None):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, params or ())
    rows = cursor.fetchall()
    cursor.close()
    return rows


def execute(sql, params=None):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(sql, params or ())
    conn.commit()
    last_id = cursor.lastrowid
    cursor.close()
    return last_id


def execute_many(sql, rows):
    conn = get_db()
    cursor = conn.cursor()
    cursor.executemany(sql, rows)
    conn.commit()
    cursor.close()

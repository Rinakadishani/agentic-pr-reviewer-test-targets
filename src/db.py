import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def search_products(keyword):
    conn = sqlite3.connect("store.db")
    query = "SELECT * FROM products WHERE name LIKE '%" + keyword + "%'"
    return conn.execute(query).fetchall()
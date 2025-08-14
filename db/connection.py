import sqlite3

def get_connection():
    return sqlite3.connect("data/finanzas.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    with open("data/init.sql", "r", encoding="utf-8") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

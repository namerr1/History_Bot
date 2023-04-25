import sqlite3

con = sqlite3.connect('hist.db')
cur = con.cursor()
result = cur.execute(f'''SELECT name FROM books
    WHERE id = "бунт"''').fetchall()
print(result)
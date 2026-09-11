import sqlite3

conn=sqlite3.connect("project.db")

#print(conn.execute("""SELECT * FROM weather where temperature_c>30""").fetchall())

print(conn.execute("""SELECT a.*,b.city FROM weather a
    JOIN locations b on a.location_id=b.location_id WHERE city="Richmond" """).fetchall())
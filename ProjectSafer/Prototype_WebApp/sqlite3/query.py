import sqlite3

conn = sqlite3.connect('smartbms.db')

c = conn.cursor()

c.execute("SELECT * FROM User")

items = c.fetchall()

print("UserID ")
print("------")
for item in items:
    print(item[0])

conn.commit()

conn.close()
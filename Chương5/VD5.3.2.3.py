import sqlite3
conn = sqlite3.connect('mydatabase.db')
conn.execute("DELETE from users where id=1")
print("Tổng số bản ghi được xóa :",conn.total_changes)
cursor = conn.execute("SElECT * FROM users")
for row in cursor:
    print(row)

conn.close()

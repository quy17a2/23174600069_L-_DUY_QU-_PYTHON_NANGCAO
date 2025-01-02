import sqlite3
conn = sqlite3.connect('mydatabase.db')
conn.execute("UPDATE users SET 'Tên' = 'Nguyễn Vân Anh' Where id = '1' ")
conn.commit()
print("Tổng số dòng được cập nhật :",conn.total_changes)
cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)
conn.close()
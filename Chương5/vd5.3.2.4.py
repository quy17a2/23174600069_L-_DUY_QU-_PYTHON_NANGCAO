import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite (sẽ tạo file cơ sở dữ liệu nếu chưa có)
conn = sqlite3.connect('my database.db')
cursor = conn.cursor()

# Tạo bảng 'users' nếu chưa tồn tại
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY,
               "Tên" TEXT,
               "Tuổi" INTEGER
               )
               ''')

# Nhập tên và tuổi người dùng
name = input("Nhập tên người dùng: ")
age = int(input("Nhập tuổi người dùng: "))

# Chèn một bản ghi vào bảng 'users' với tên và tuổi người dùng
cursor.execute('''
               INSERT INTO users ("Tên", "Tuổi")
               VALUES (?, ?)
               ''', (name, age))

# Commit thay đổi vào cơ sở dữ liệu
conn.commit()

# Truy vấn tất cả bản ghi từ bảng 'users'
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# In ra tất cả các bản ghi
for row in rows:
    print(row)

# Đóng cursor và kết nối
cursor.close()
conn.close()

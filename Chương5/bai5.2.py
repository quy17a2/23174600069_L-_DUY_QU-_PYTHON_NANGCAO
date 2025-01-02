import sqlite3

def connect_in_memory_db():
    try:
        
        conn = sqlite3.connect(':memory:')
        print("Kết nối đến cơ sở dữ liệu SQLite trong bộ nhớ thành công.")
        return conn
    except sqlite3.Error as e:
        print(f"Lỗi khi kết nối đến SQLite trong bộ nhớ: {e}")
        return None

def get_sqlite_version(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT sqlite_version();")
        version = cursor.fetchone()[0]
        return version
    except sqlite3.Error as e:
        print(f"Lỗi khi truy vấn phiên bản SQLite: {e}")
        return None

def main():
    conn = connect_in_memory_db()

    if conn:
        version = get_sqlite_version(conn)
        if version:
            print(f"Phiên bản SQLite hiện tại: {version}")
        conn.close()
        print("Đã đóng kết nối đến cơ sở dữ liệu.")

if __name__ == "__main__":
    main()

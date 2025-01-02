import sqlite3

def create_and_connect_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Kết nối đến cơ sở dữ liệu '{db_name}' thành công.")
        return conn
    except sqlite3.Error as e:
        print(f"Lỗi khi kết nối đến SQLite: {e}")
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
    database_name = "my_database.db" 
    conn = create_and_connect_db(database_name)

    if conn:
        version = get_sqlite_version(conn)
        if version:
            print(f"Phiên bản SQLite hiện tại: {version}")
        conn.close()
        print("Đã đóng kết nối đến cơ sở dữ liệu.")

if __name__ == "__main__":
    main()

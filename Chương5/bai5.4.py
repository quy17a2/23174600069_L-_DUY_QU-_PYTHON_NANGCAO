import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """
    Tạo kết nối đến cơ sở dữ liệu SQLite.
    
    :param db_file: Đường dẫn tới file cơ sở dữ liệu.
    :return: Đối tượng kết nối hoặc None nếu kết nối thất bại.
    """
    if not os.path.exists(db_file):
        print(f"File cơ sở dữ liệu '{db_file}' không tồn tại.")
        return None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Kết nối thành công đến cơ sở dữ liệu '{db_file}'.")
    except Error as e:
        print(f"Lỗi kết nối đến SQLite: {e}")
    return conn

def list_tables(conn):
    """
    Liệt kê tất cả các bảng trong cơ sở dữ liệu SQLite.
    
    :param conn: Đối tượng kết nối đến cơ sở dữ liệu.
    :return: Danh sách tên các bảng hoặc None nếu có lỗi.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = cursor.fetchall()
        if tables:
            print("Danh sách các bảng trong cơ sở dữ liệu:")
            for table in tables:
                print(f"- {table[0]}")
            return [table[0] for table in tables]
        else:
            print("Không tìm thấy bảng nào trong cơ sở dữ liệu.")
            return []
    except Error as e:
        print(f"Lỗi khi truy vấn danh sách bảng: {e}")
        return None

def main():
    db_file = input("Nhập đường dẫn tới file cơ sở dữ liệu SQLite (ví dụ: example.db): ").strip()
    conn = create_connection(db_file)
    
    if conn:
        list_tables(conn)
        conn.close()
        print("Đã đóng kết nối đến cơ sở dữ liệu.")
    else:
        print("Không thể kết nối đến cơ sở dữ liệu. Vui lòng kiểm tra lại đường dẫn.")

if __name__ == "__main__":
    main()

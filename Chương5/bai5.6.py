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

def table_exists(conn, table_name):
    """
    Kiểm tra xem một bảng có tồn tại trong cơ sở dữ liệu không.

    :param conn: Đối tượng kết nối đến cơ sở dữ liệu.
    :param table_name: Tên bảng cần kiểm tra.
    :return: True nếu bảng tồn tại, False nếu không tồn tại hoặc có lỗi.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name=?;
        """, (table_name,))
        result = cursor.fetchone()
        if result:
            print(f"Bảng '{table_name}' tồn tại trong cơ sở dữ liệu.")
            return True
        else:
            print(f"Bảng '{table_name}' không tồn tại trong cơ sở dữ liệu.")
            return False
    except Error as e:
        print(f"Lỗi khi kiểm tra sự tồn tại của bảng: {e}")
        return False

def count_records(conn, table_name):
    """
    Đếm số lượng bản ghi trong một bảng cụ thể.

    :param conn: Đối tượng kết nối đến cơ sở dữ liệu.
    :param table_name: Tên bảng cần đếm bản ghi.
    :return: Số lượng bản ghi hoặc None nếu có lỗi.
    """
    try:
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM {table_name};"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        return count
    except Error as e:
        print(f"Lỗi khi đếm bản ghi trong bảng '{table_name}': {e}")
        return None
    except sqlite3.OperationalError as oe:
        print(f"Lỗi truy vấn: {oe}")
        return None

def main():
    # Yêu cầu người dùng nhập đường dẫn tới file cơ sở dữ liệu SQLite
    db_file = input("Nhập đường dẫn tới file cơ sở dữ liệu SQLite (ví dụ: school.db): ").strip()

    # Tạo kết nối đến cơ sở dữ liệu
    conn = create_connection(db_file)

    if conn:
        try:
            # Yêu cầu người dùng nhập tên bảng
            table_name = input("Nhập tên bảng để đếm số bản ghi (ví dụ: students): ").strip()

            # Kiểm tra xem bảng có tồn tại không
            if table_exists(conn, table_name):
                # Đếm số bản ghi trong bảng
                count = count_records(conn, table_name)
                if count is not None:
                    print(f"\nSố lượng bản ghi trong bảng '{table_name}': {count}")
        finally:
            # Đóng kết nối sau khi sử dụng xong
            conn.close()
            print("\nĐã đóng kết nối đến cơ sở dữ liệu.")
    else:
        print("Không thể kết nối đến cơ sở dữ liệu. Vui lòng kiểm tra lại đường dẫn.")

if __name__ == "__main__":
    main()

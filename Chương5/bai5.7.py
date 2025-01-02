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

def column_exists(conn, table_name, column_name):
    """
    Kiểm tra xem một cột có tồn tại trong bảng không.

    :param conn: Đối tượng kết nối đến cơ sở dữ liệu.
    :param table_name: Tên bảng chứa cột.
    :param column_name: Tên cột cần kiểm tra.
    :return: True nếu cột tồn tại, False nếu không tồn tại hoặc có lỗi.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        for column in columns:
            if column[1] == column_name:
                print(f"Cột '{column_name}' tồn tại trong bảng '{table_name}'.")
                return True
        print(f"Cột '{column_name}' không tồn tại trong bảng '{table_name}'.")
        return False
    except Error as e:
        print(f"Lỗi khi kiểm tra sự tồn tại của cột: {e}")
        return False

def update_column_values(conn, table_name, column_name, new_value):
    """
    Cập nhật tất cả các giá trị của một cột cụ thể trong bảng.

    :param conn: Đối tượng kết nối đến cơ sở dữ liệu.
    :param table_name: Tên bảng chứa cột cần cập nhật.
    :param column_name: Tên cột cần cập nhật.
    :param new_value: Giá trị mới để cập nhật vào cột.
    :return: Số lượng bản ghi đã được cập nhật hoặc None nếu có lỗi.
    """
    try:
        cursor = conn.cursor()
        query = f"UPDATE {table_name} SET {column_name} = ?;"
        cursor.execute(query, (new_value,))
        conn.commit()
        updated_rows = cursor.rowcount
        return updated_rows
    except Error as e:
        print(f"Lỗi khi cập nhật giá trị trong cột '{column_name}' của bảng '{table_name}': {e}")
        return None

def main():
    db_file = input("Nhập đường dẫn tới file cơ sở dữ liệu SQLite (ví dụ: school.db): ").strip()
    conn = create_connection(db_file)

    if conn:
        try:
            table_name = input("Nhập tên bảng để cập nhật cột (ví dụ: students): ").strip()

            
            if not table_exists(conn, table_name):
                return

            
            column_name = input("Nhập tên cột cần cập nhật (ví dụ: grade): ").strip()

            
            if not column_exists(conn, table_name, column_name):
                return

            
            new_value = input(f"Nhập giá trị mới để cập nhật vào cột '{column_name}': ").strip()

            
            updated_rows = update_column_values(conn, table_name, column_name, new_value)

            if updated_rows is not None:
                print(f"\nĐã cập nhật {updated_rows} bản ghi trong cột '{column_name}' của bảng '{table_name}' thành '{new_value}'.")
        finally:
            
            conn.close()
            print("\nĐã đóng kết nối đến cơ sở dữ liệu.")
    else:
        print("Không thể kết nối đến cơ sở dữ liệu. Vui lòng kiểm tra lại đường dẫn.")

if __name__ == "__main__":
    main()

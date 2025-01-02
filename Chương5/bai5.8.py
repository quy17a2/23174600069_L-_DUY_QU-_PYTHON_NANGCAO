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

def list_records(conn, table_name):
    """
    Liệt kê tất cả các bản ghi trong bảng.

    :param conn: Đối tượng kết nối đến cơ sở dữ liệu.
    :param table_name: Tên bảng để liệt kê bản ghi.
    :return: Danh sách các bản ghi hoặc None nếu có lỗi.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if rows:
            print(f"\nDanh sách các bản ghi trong bảng '{table_name}':")
            # Lấy tên cột
            column_names = [description[0] for description in cursor.description]
            print(" | ".join(column_names))
            print("-" * 50)
            for row in rows:
                print(" | ".join([str(item) for item in row]))
            return rows
        else:
            print(f"Không có bản ghi nào trong bảng '{table_name}'.")
            return []
    except Error as e:
        print(f"Lỗi khi truy vấn bản ghi: {e}")
        return None

def delete_record(conn, table_name, record_id):
    """
    Xóa một bản ghi cụ thể dựa trên ID.

    :param conn: Đối tượng kết nối đến cơ sở dữ liệu.
    :param table_name: Tên bảng chứa bản ghi cần xóa.
    :param record_id: ID của bản ghi cần xóa.
    :return: Số lượng bản ghi đã xóa hoặc None nếu có lỗi.
    """
    try:
        cursor = conn.cursor()
        # Giả sử cột khóa chính là 'id'
        sql = f"DELETE FROM {table_name} WHERE id = ?;"
        cursor.execute(sql, (record_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(f"Lỗi khi xóa bản ghi với ID = {record_id}: {e}")
        return None

def main():
    # Yêu cầu người dùng nhập đường dẫn tới file cơ sở dữ liệu SQLite
    db_file = input("Nhập đường dẫn tới file cơ sở dữ liệu SQLite (ví dụ: school.db): ").strip()

    # Tạo kết nối đến cơ sở dữ liệu
    conn = create_connection(db_file)

    if conn:
        try:
            
            table_name = input("Nhập tên bảng để xóa bản ghi (ví dụ: students): ").strip()

        
            if not table_exists(conn, table_name):
                return

            
            records = list_records(conn, table_name)
            if records is None:
                return
            elif len(records) == 0:
                return

            
            record_id_input = input("\nNhập ID của bản ghi cần xóa: ").strip()
            if not record_id_input.isdigit():
                print("ID phải là một số nguyên.")
                return
            record_id = int(record_id_input)

            
            record_exists = False
            for record in records:
                if record[0] == record_id:
                    record_exists = True
                    break
            if not record_exists:
                print(f"Không tìm thấy bản ghi với ID = {record_id}.")
                return

            
            confirm = input(f"Bạn có chắc chắn muốn xóa bản ghi với ID = {record_id}? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Hành động xóa đã bị hủy.")
                return

            
            deleted_rows = delete_record(conn, table_name, record_id)
            if deleted_rows is not None:
                if deleted_rows > 0:
                    print(f"Đã xóa {deleted_rows} bản ghi với ID = {record_id} từ bảng '{table_name}'.")
                else:
                    print(f"Không có bản ghi nào được xóa.")
        finally:
        
            conn.close()
            print("\nĐã đóng kết nối đến cơ sở dữ liệu.")
    else:
        print("Không thể kết nối đến cơ sở dữ liệu. Vui lòng kiểm tra lại đường dẫn.")

if __name__ == "__main__":
    main()

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
    Tạo kết nối đến cơ sở dữ liệu SQLite.
    
    :param db_file: Đường dẫn tới file cơ sở dữ liệu.
    :return: Đối tượng kết nối hoặc None nếu kết nối thất bại.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Kết nối thành công đến cơ sở dữ liệu '{db_file}'.")
    except Error as e:
        print(f"Lỗi kết nối đến SQLite: {e}")
    return conn

def create_table(conn, create_table_sql):
    """
    Tạo bảng trong cơ sở dữ liệu SQLite.
    
    :param conn: Đối tượng kết nối.
    :param create_table_sql: Câu lệnh SQL để tạo bảng.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Đã tạo bảng thành công.")
    except Error as e:
        print(f"Lỗi tạo bảng: {e}")

def main():
    # Đường dẫn tới file cơ sở dữ liệu SQLite
    database = "example.db"

    # Câu lệnh SQL để tạo bảng "employees"
    sql_create_employees_table = """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL,
        hire_date TEXT
    );
    """

    # Tạo kết nối đến cơ sở dữ liệu
    conn = create_connection(database)

    # Nếu kết nối thành công, tiến hành tạo bảng
    if conn is not None:
        create_table(conn, sql_create_employees_table)
        
        # Bạn có thể thêm các thao tác khác ở đây, ví dụ: thêm dữ liệu, truy vấn dữ liệu, v.v.
        
        # Đóng kết nối sau khi hoàn thành
        conn.close()
        print("Đã đóng kết nối đến cơ sở dữ liệu.")
    else:
        print("Không thể kết nối đến cơ sở dữ liệu.")

if __name__ == "__main__":
    main()

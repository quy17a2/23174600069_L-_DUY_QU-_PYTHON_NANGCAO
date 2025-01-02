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

def insert_records(conn, records):
    """
    Chèn nhiều bản ghi vào bảng.

    :param conn: Đối tượng kết nối.
    :param records: Danh sách các tuple chứa dữ liệu bản ghi.
    """
    sql = ''' INSERT INTO students(name, age, grade)
              VALUES(?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, records)
        conn.commit()
        print(f"Đã chèn {cursor.rowcount} bản ghi vào bảng 'students'.")
    except Error as e:
        print(f"Lỗi chèn bản ghi: {e}")

def select_all_records(conn):
    """
    Chọn tất cả các bản ghi từ bảng và hiển thị chúng.

    :param conn: Đối tượng kết nối.
    :return: Danh sách các bản ghi hoặc None nếu có lỗi.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")

        rows = cursor.fetchall()

        if rows:
            print("\nDanh sách các bản ghi trong bảng 'students':")
            print("{:<5} {:<20} {:<5} {:<10}".format('ID', 'Tên', 'Tuổi', 'Lớp'))
            print("-" * 40)
            for row in rows:
                print("{:<5} {:<20} {:<5} {:<10}".format(row[0], row[1], row[2], row[3]))
        else:
            print("Không có bản ghi nào trong bảng 'students'.")
    except Error as e:
        print(f"Lỗi truy vấn bản ghi: {e}")

def main():
    database = "school.db"

    # Câu lệnh SQL để tạo bảng 'students'
    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    );
    """

    # Dữ liệu để chèn vào bảng 'students'
    students = [
        ("Nguyễn Văn A", 20, "10A"),
        ("Trần Thị B", 19, "10B"),
        ("Lê Văn C", 21, "11A"),
        ("Phạm Thị D", 22, "12B")
    ]

    # Tạo kết nối đến cơ sở dữ liệu
    conn = create_connection(database)

    if conn:
        # Tạo bảng 'students'
        create_table(conn, sql_create_students_table)

        # Chèn bản ghi vào bảng 'students'
        insert_records(conn, students)

        # Chọn và hiển thị tất cả các bản ghi
        select_all_records(conn)

        # Đóng kết nối
        conn.close()
        print("\nĐã đóng kết nối đến cơ sở dữ liệu.")
    else:
        print("Không thể kết nối đến cơ sở dữ liệu.")

if __name__ == "__main__":
    main()

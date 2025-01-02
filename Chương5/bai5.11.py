import sqlite3
from sqlite3 import Error

def create_connection(db_file="ql_nhan_vien.db"):
    """
    Tạo (hoặc mở) kết nối đến CSDL SQLite.
    Nếu chưa có file ql_nhan_vien.db thì sẽ được tạo mới.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # Bật chế độ hỗ trợ khóa ngoại
        conn.execute("PRAGMA foreign_keys = 1")
        print(f"Đã kết nối (hoặc tạo mới) CSDL '{db_file}' thành công.")
    except Error as e:
        print(f"Lỗi kết nối đến SQLite: {e}")
    return conn

def create_table_phong(conn):
    """
    Tạo bảng PHONG (nếu chưa tồn tại).
    """
    try:
        sql_phong = """
        CREATE TABLE IF NOT EXISTS PHONG (
            id INTEGER PRIMARY KEY,
            ten_phong TEXT NOT NULL
            -- bạn có thể thêm cột mo_ta v.v. nếu cần
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_phong)
        conn.commit()
        print("Bảng 'PHONG' đã được tạo (nếu chưa có).")
    except Error as e:
        print(f"Lỗi khi tạo bảng PHONG: {e}")

def create_table_nhan_vien(conn):
    """
    Tạo bảng NHAN_VIEN (nếu chưa tồn tại).
    """
    try:
        sql_nv = """
        CREATE TABLE IF NOT EXISTS NHAN_VIEN (
            id INTEGER PRIMARY KEY,
            ho_ten TEXT NOT NULL,
            tuoi INTEGER NOT NULL,
            dia_chi TEXT NOT NULL,
            luong REAL NOT NULL,
            id_phong INTEGER NOT NULL,
            FOREIGN KEY (id_phong) REFERENCES PHONG(id)
                ON DELETE CASCADE 
                ON UPDATE CASCADE
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_nv)
        conn.commit()
        print("Bảng 'NHAN_VIEN' đã được tạo (nếu chưa có).")
    except Error as e:
        print(f"Lỗi khi tạo bảng NHAN_VIEN: {e}")

def main():
    # 1. Kết nối CSDL ql_nhan_vien.db
    conn = create_connection("ql_nhan_vien.db")
    if conn is None:
        print("Kết nối CSDL thất bại. Kết thúc.")
        return

    # 2. Tạo bảng PHONG
    create_table_phong(conn)

    # 3. Tạo bảng NHAN_VIEN
    create_table_nhan_vien(conn)

    # Đóng kết nối
    conn.close()
    print("Đã đóng kết nối đến CSDL.")

if __name__ == "__main__":
    main()

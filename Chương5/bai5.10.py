import sqlite3
from sqlite3 import Error
def create_connection(db_file="product.db"):
    """Tạo kết nối đến cơ sở dữ liệu SQLite. 
       Nếu file product.db chưa tồn tại, sẽ được tạo mới."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(f"Lỗi kết nối đến SQLite: {e}")
    return conn
def create_table_product(conn):
    """Tạo bảng product nếu chưa tồn tại."""
    try:
        sql_create_product_table = """
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            amount INTEGER NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_product_table)
        conn.commit()
        print("Bảng 'product' đã sẵn sàng.")
    except Error as e:
        print(f"Lỗi tạo bảng product: {e}")
def show_all_products(conn):
    """Lấy tất cả sản phẩm từ bảng product và in ra."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()

        if rows:
            print("\nDanh sách sản phẩm:")
            print("{:<5} {:<20} {:<10} {:<10}".format("ID", "NAME", "PRICE", "AMOUNT"))
            print("-" * 50)
            for row in rows:
                print("{:<5} {:<20} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
        else:
            print("\nChưa có sản phẩm nào trong CSDL.")
    except Error as e:
        print(f"Lỗi khi đọc danh sách sản phẩm: {e}")
def add_product(conn):
    """Thêm một sản phẩm mới với id, name, price, amount."""
    try:
        pid = input("Nhập ID (số nguyên): ").strip()
        name = input("Nhập tên sản phẩm: ").strip()
        price = input("Nhập đơn giá (số thực): ").strip()
        amount = input("Nhập số lượng (số nguyên): ").strip()
        pid = int(pid)
        price = float(price)
        amount = int(amount)
        sql_insert = """
        INSERT INTO product(id, name, price, amount)
        VALUES (?, ?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(sql_insert, (pid, name, price, amount))
        conn.commit()
        print(f"Đã thêm sản phẩm '{name}' thành công.")
    except ValueError:
        print("Dữ liệu nhập không hợp lệ (ID, price, amount phải là số).")
    except sqlite3.IntegrityError:
        print("ID bị trùng hoặc vi phạm ràng buộc. Vui lòng thử lại.")
    except Error as e:
        print(f"Lỗi khi thêm sản phẩm: {e}")
def search_by_name(conn):
    """Tìm sản phẩm theo từ khóa tên (có thể một phần)"""
    keyword = input("Nhập từ khóa tên sản phẩm: ").strip()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM product WHERE name LIKE ?"
        cursor.execute(query, (f"%{keyword}%",))
        rows = cursor.fetchall()

        if rows:
            print("\nKết quả tìm kiếm:")
            print("{:<5} {:<20} {:<10} {:<10}".format("ID", "NAME", "PRICE", "AMOUNT"))
            print("-" * 50)
            for row in rows:
                print("{:<5} {:<20} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
        else:
            print("Không tìm thấy sản phẩm phù hợp.")
    except Error as e:
        print(f"Lỗi khi tìm kiếm: {e}")
def update_product(conn):
    """Cập nhật price, amount cho sản phẩm dựa trên id."""
    try:
        pid = input("Nhập ID sản phẩm cần cập nhật: ").strip()
        new_price = input("Nhập đơn giá mới (số thực): ").strip()
        new_amount = input("Nhập số lượng mới (số nguyên): ").strip()

        pid = int(pid)
        new_price = float(new_price)
        new_amount = int(new_amount)

        sql_update = "UPDATE product SET price = ?, amount = ? WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(sql_update, (new_price, new_amount, pid))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Đã cập nhật sản phẩm có ID = {pid}.")
        else:
            print(f"Không tìm thấy sản phẩm ID = {pid}.")
    except ValueError:
        print("Dữ liệu nhập không hợp lệ (ID, price, amount phải là số).")
    except Error as e:
        print(f"Lỗi khi cập nhật sản phẩm: {e}")
def delete_product(conn):
    """Xóa sản phẩm dựa trên id."""
    try:
        pid = input("Nhập ID sản phẩm cần xóa: ").strip()
        pid = int(pid)

        cursor = conn.cursor()
        sql_delete = "DELETE FROM product WHERE id = ?"
        cursor.execute(sql_delete, (pid,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Đã xóa sản phẩm có ID = {pid}.")
        else:
            print(f"Không tìm thấy sản phẩm có ID = {pid}.")
    except ValueError:
        print("ID phải là số nguyên.")
    except Error as e:
        print(f"Lỗi khi xóa sản phẩm: {e}")
def main():
    conn = create_connection("product.db")
    if conn is None:
        print("Không thể kết nối CSDL. Kết thúc chương trình.")
        return
    create_table_product(conn)

    while True:
        print("\n--- QUẢN LÝ SẢN PHẨM ---")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật đơn giá và số lượng")
        print("5. Xóa sản phẩm theo ID")
        print("6. Thoát chương trình")

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == '1':
            show_all_products(conn)
        elif choice == '2':
            add_product(conn)
        elif choice == '3':
            search_by_name(conn)
        elif choice == '4':
            update_product(conn)
        elif choice == '5':
            delete_product(conn)
        elif choice == '6':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
    conn.close()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox


def cac_uoc_cua_so_nguyen(n):
    """
    Liệt kê tất cả các ước của một số nguyên N.

    Args:
        n: Số nguyên N.

    Returns:
        Mảng chứa tất cả các ước của N.
    """
    uocs = []
    for i in range(1, n + 1):
        if n % i == 0:
            uocs.append(i)
    return uocs


def xuat_cac_uoc(entry_n, entry_ketqua):
    """
    Xuất tất cả các ước của số nguyên N.

    Args:
        entry_n: Widget nhập số nguyên N.
        entry_ketqua: Widget hiển thị kết quả.
    """
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("Số phải là số nguyên dương.")
        uocs = cac_uoc_cua_so_nguyen(n)
        entry_ketqua.delete(0, tk.END)
        entry_ketqua.insert(0, " ".join(map(str, uocs)))
    except ValueError as e:
        messagebox.showerror("Lỗi nhập liệu", f"Vui lòng nhập một số nguyên hợp lệ. Chi tiết: {e}")


def main():
    root = tk.Tk()
    root.title("Liệt kê các ước của một số nguyên")

    # Nhãn và ô nhập số nguyên
    label_n = tk.Label(root, text="Nhập giá trị của N:")
    entry_n = tk.Entry(root)
    label_n.grid(row=0, column=0, padx=10, pady=5)
    entry_n.grid(row=0, column=1, padx=10, pady=5)

    # Nhãn và ô hiển thị kết quả
    label_ketqua = tk.Label(root, text="Các ước của N là:")
    entry_ketqua = tk.Entry(root)
    label_ketqua.grid(row=1, column=0, padx=10, pady=5)
    entry_ketqua.grid(row=1, column=1, padx=10, pady=5)

    # Nút xác nhận
    button_submit = tk.Button(
        root,
        text="Xác nhận",
        command=lambda: xuat_cac_uoc(entry_n, entry_ketqua),
    )
    button_submit.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
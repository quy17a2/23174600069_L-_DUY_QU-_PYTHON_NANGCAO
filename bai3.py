class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        if not self.kiem_tra_hop_le():
            raise ValueError("Mẫu số không được bằng 0!")

    def kiem_tra_hop_le(self):
        """Kiểm tra tính hợp lệ của phân số"""
        return self.mau_so != 0

    def nhap_phan_so(self):
        """Nhập phân số từ người dùng"""
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        if not self.kiem_tra_hop_le():
            raise ValueError("Mẫu số không được bằng 0!")

    def in_phan_so(self):
        """In phân số ra màn hình"""
        print(f"Phân số: {self.tu_so}/{self.mau_so}")

def main():
    try:
        phan_so = PhanSo()
        phan_so.nhap_phan_so()
        phan_so.in_phan_so()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

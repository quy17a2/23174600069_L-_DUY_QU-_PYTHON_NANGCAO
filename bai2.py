class SinhVien:
    def __init__(self):
        self.ten = ""
        self.diem_toan = 0
        self.diem_vat_ly = 0
        self.diem_hoa_hoc = 0
        self.diem_tong = 0

    def nhap_thong_tin(self):
        self.ten = input("Nhập tên sinh viên: ")
        self.diem_toan = float(input("Nhập điểm toán của sinh viên: "))
        self.diem_vat_ly = float(input("Nhập điểm vật lý của sinh viên: "))
        self.diem_hoa_hoc = float(input("Nhập điểm hóa học của sinh viên: "))
        self.tinh_diem_tong()

    def in_thong_tin(self):
        print("Thông tin sinh viên:")
        print(f"Tên: {self.ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Vật Lý: {self.diem_vat_ly}")
        print(f"Điểm Hóa Học: {self.diem_hoa_hoc}")
        print(f"Điểm Tổng: {self.diem_tong}")

    def tinh_diem_tong(self):
        self.diem_tong = self.diem_toan + self.diem_vat_ly + self.diem_hoa_hoc

def main():
    danh_sach_sinh_vien = []
    so_sinh_vien = int(input("Nhập số lượng sinh viên: "))

    for i in range(so_sinh_vien):
        sinh_vien = SinhVien()
        sinh_vien.nhap_thong_tin()
        danh_sach_sinh_vien.append(sinh_vien)

    danh_sach_sinh_vien.sort(key=lambda x: x.diem_tong, reverse=True)

    print("Danh sách sinh viên đã vượt qua ngưỡng nhập học:")
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien.diem_tong >= 20:
            sinh_vien.in_thong_tin()
            print()

if __name__ == "__main__":
    main()

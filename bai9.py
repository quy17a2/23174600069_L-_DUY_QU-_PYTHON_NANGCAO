class DaGiac:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh

    def chu_vi(self):
        raise NotImplementedError("Phương thức này phải được cài đặt trong lớp kế thừa.")

    def dien_tich(self):
        raise NotImplementedError("Phương thức này phải được cài đặt trong lớp kế thừa.")

class HinhBinhHanh(DaGiac):
    def __init__(self, canh_a, canh_b, chieu_cao):
        super().__init__(4)  
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.chieu_cao = chieu_cao

    def chu_vi(self):
        return 2 * (self.canh_a + self.canh_b)

    def dien_tich(self):
        return self.canh_a * self.chieu_cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_rong)  

    def chu_vi(self):
        return 2 * (self.canh_a + self.canh_b)  
    def dien_tich(self):
        return self.canh_a * self.canh_b

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)  

def main():
    print("Nhập thông tin cho hình bình hành:")
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    h = float(input("Nhập chiều cao: "))
    hinh_binh_hanh = HinhBinhHanh(a, b, h)
    print(f"Chu vi hình bình hành: {hinh_binh_hanh.chu_vi()}")
    print(f"Diện tích hình bình hành: {hinh_binh_hanh.dien_tich()}")

    print("\nNhập thông tin cho hình chữ nhật:")
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    hinh_chu_nhat = HinhChuNhat(dai, rong)
    print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.chu_vi()}")
    print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.dien_tich()}")

    print("\nNhập thông tin cho hình vuông:")
    canh = float(input("Nhập cạnh: "))
    hinh_vuong = HinhVuong(canh)
    print(f"Chu vi hình vuông: {hinh_vuong.chu_vi()}")
    print(f"Diện tích hình vuông: {hinh_vuong.dien_tich()}")

if __name__ == "__main__":
    main()

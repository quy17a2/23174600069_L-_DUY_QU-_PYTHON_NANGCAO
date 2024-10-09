class Ngay:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def __str__(self):
        """Trả về chuỗi định dạng ngày/tháng/năm"""
        return f"{self.ngay}/{self.thang}/{self.nam}"

class NhanVien:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty, phong_ban, chuc_vu):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cong_ty = ngay_vao_cong_ty
        self.phong_ban = phong_ban
        self.chuc_vu = chuc_vu

    def __str__(self):
        """Trả về thông tin nhân viên"""
        return f"Nhân viên: {self.ho_ten}\n" \
               f"Ngày sinh: {self.ngay_sinh}\n" \
               f"Ngày vào công ty: {self.ngay_vao_cong_ty}\n" \
               f"Phòng ban: {self.phong_ban}\n" \
               f"Chức vụ: {self.chuc_vu}"

# Ví dụ sử dụng
def main():
    # Tạo một đối tượng Ngày cho ngày sinh và ngày vào công ty
    ngay_sinh = Ngay(15, 5, 1990)
    ngay_vao_cong_ty = Ngay(1, 1, 2020)

    # Tạo một đối tượng Nhân viên
    nhan_vien = NhanVien("Nguyễn Văn A", ngay_sinh, ngay_vao_cong_ty, "Kế toán", "Nhân viên")

    # In thông tin nhân viên
    print(nhan_vien)

if __name__ == "__main__":
    main()

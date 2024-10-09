class Ngay:
    def __init__(self, ngay=3, thang=3, nam=2024):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def hien_thi(self):
        """In thông tin về ngày ra màn hình"""
        print(f"Ngày: {self.ngay:02d}/{self.thang:02d}/{self.nam}")

    def ngay_tiep_theo(self):
        """Tính ngày tiếp theo"""
        if self.nam_nhuan(self.nam) and self.thang == 2:
            so_ngay_trong_thang = 29
        else:
            so_ngay_trong_thang = self.so_ngay_trong_thang(self.thang)

        if self.ngay < so_ngay_trong_thang:
            self.ngay += 1
        else:
            self.ngay = 1
            if self.thang == 12:
                self.thang = 1
                self.nam += 1
            else:
                self.thang += 1

    @staticmethod
    def so_ngay_trong_thang(thang):
        """Trả về số ngày trong tháng"""
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif thang in [4, 6, 9, 11]:
            return 30
        else:
            return 28  
    @staticmethod
    def nam_nhuan(nam):
        """Kiểm tra năm nhuận"""
        return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def main():
    
    ngay = Ngay()
    ngay.hien_thi()

    
    ngay.ngay_tiep_theo()
    print("Ngày tiếp theo:")
    ngay.hien_thi()

if __name__ == "__main__":
    main()

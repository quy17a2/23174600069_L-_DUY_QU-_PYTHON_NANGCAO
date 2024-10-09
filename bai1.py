class Hình_Chữ_Nhật:
    def __init__(self):
        self.length = 0
        self.width = 0

    def input_data(self):
        self.length = float(input("Nhập độ dài của hình chữ nhật: "))
        self.width = float(input("Nhập độ rộng của hình chữ nhật: "))

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

    def print_info(self):
        print("Thông Tin Hình Chữ Nhật:")
        print(f"Độ Dài: {self.length}")
        print(f"Độ Rộng: {self.width}")
        print(f"Chu Vi: {self.calculate_perimeter()}")
        print(f"Diện Tích: {self.calculate_area()}")
def main():
    hình_chữ_nhật = Hình_Chữ_Nhật()
    hình_chữ_nhật.input_data()
    hình_chữ_nhật.print_info()

if __name__ == "__main__":
    main()
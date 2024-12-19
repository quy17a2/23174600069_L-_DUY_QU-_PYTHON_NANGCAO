import json

class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_json(self):
        try:
            # Đọc nội dung tệp
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()  # Loại bỏ khoảng trắng thừa
                if not content:  # Tệp rỗng
                    print(f"Error: File '{self.file_path}' is empty.")
                    self.data = None
                    return
                self.data = json.loads(content)  # Phân tích cú pháp JSON
        except FileNotFoundError:
            print(f"Error: File not found at '{self.file_path}'")
            self.data = None
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON. Reason: {e}")
            self.data = None

    def display_data(self):
        if not self.data:
            print("No data available.")
            return
        for user in self.data:
            print(f"Name: {user['name']}, Age: {user['age']}, Address: {user['address']}")

# Đường dẫn đến tệp JSON
path = r'D:\bài tập thực hành\lab1\users.json'

# Tạo đối tượng JSONReader và đọc/hiển thị dữ liệu
reader = JSONReader(path)
reader.read_json()
reader.display_data()

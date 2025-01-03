import tkinter as tk
from PIL import Image, ImageTk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chương trình xem ảnh")

# Mở và xử lý ảnh
try:
    image = Image.open("oto.png")  
    new_size = (400, 300)  
    image = image.resize(new_size, Image.Resampling.LANCZOS)  # Thay ANTIALIAS bằng Resampling.LANCZOS

    img = ImageTk.PhotoImage(image)

    label = tk.Label(window, image=img)
    label.image = img
    label.pack()

except FileNotFoundError:
    error_label = tk.Label(window, text="Không tìm thấy file ảnh 'oto.png'", fg="red")
    error_label.pack()


window.mainloop()
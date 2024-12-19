import numpy as np


np.random.seed(42)  
temperatures = np.round(np.random.uniform(low=15, high=35, size=30), 2)  


average_temp = np.mean(temperatures)
print("Dữ liệu nhiệt độ hàng ngày trong tháng:", temperatures)
print(f"Nhiệt độ trung bình trong tháng: {average_temp:.2f}°C")

max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
max_temp_day = np.argmax(temperatures) + 1 
min_temp_day = np.argmin(temperatures) + 1  

print(f"Nhiệt độ cao nhất: {max_temp}°C vào ngày {max_temp_day}")
print(f"Nhiệt độ thấp nhất: {min_temp}°C vào ngày {min_temp_day}")


temp_diff = np.abs(np.diff(temperatures))  
max_diff = np.max(temp_diff)
max_diff_day = np.argmax(temp_diff) + 1  

print(f"Sự chênh lệch nhiệt độ cao nhất là {max_diff:.2f}°C, từ ngày {max_diff_day} đến ngày {max_diff_day + 1}")

above_20 = np.where(temperatures > 20)[0] + 1
print(f"Các ngày có nhiệt độ trên 20°C: {above_20}")


selected_days = [5, 10, 15, 20, 25]
selected_temps = temperatures[[day - 1 for day in selected_days]]
print(f"Nhiệt độ các ngày 5, 10, 15, 20, 25: {selected_temps}")

above_avg_days = np.where(temperatures > average_temp)[0] + 1
above_avg_temps = temperatures[temperatures > average_temp]
print(f"Các ngày có nhiệt độ trên trung bình ({average_temp:.2f}°C): {above_avg_days}, Nhiệt độ: {above_avg_temps}")

even_days_temps = temperatures[1::2]  
odd_days_temps = temperatures[0::2]  
print(f"Nhiệt độ các ngày chẵn: {even_days_temps}")
print(f"Nhiệt độ các ngày lẻ: {odd_days_temps}")

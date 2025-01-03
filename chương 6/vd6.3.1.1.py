import threading
def my_funtion(arg):
    print("đối số là: ",arg)
    print("Đây là luồng đang chạy!! ")
my_thread = threading.Thread(target=my_funtion,args=(10,))
my_thread.start()
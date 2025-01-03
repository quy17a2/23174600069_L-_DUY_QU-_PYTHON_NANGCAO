import threading

def inso(limit):
    for i in range(0, limit + 1, 2): 
        print(f"Even: {i}")

def soluong(limit):
    for i in range(1, limit + 1, 2):
        print(f"Odd: {i}")

LIMIT = 20  

even_thread = threading.Thread(target=inso, args=(LIMIT,))
odd_thread = threading.Thread(target=soluong, args=(LIMIT,))

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Xong!")

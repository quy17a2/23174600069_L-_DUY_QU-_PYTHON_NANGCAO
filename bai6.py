class Ngăn_Xếp:
    def __init__(self, capacity=10):
        self.data = [0.0] * capacity
        self.size = 0
        self.capacity = capacity

    def __del__(self):
        del self.data

    def push(self, element):
        if self.isFull():
            print("Ngăn xếp đầy. Không thể đẩy phần tử.")
            return
        self.data[self.size] = element
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống. Không thể lấy phần tử.")
            return
        element = self.data[self.size - 1]
        self.size -= 1
        return element

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def count(self):
        return self.size

    def print(self):
        print("Ngăn xếp:", end=" ")
        for i in range(self.size):
            print(self.data[i], end=" ")
        print()
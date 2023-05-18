#тератори
"""lst = [1,2,3,4,5,6,7]
print(iter(lst))"""

#1
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
my_list = [1,2,3,4,5,6,7]
my_iter = MyIterator(my_list)
for num in my_list:
    print(num)
print()

#2
def my_generator(data):
    for item in data:
        yield item
for num in my_generator(my_list):
    print(num)
print()

#3
def cal():
    def add(a, b):
        return a + b
    def minus(a, b):
        return a - b
    def mnog(a, b):
        return a * b
    def dilen(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Bro💀")
    return add, minus, mnog, dilen
add, minus, mnog, dilen = cal()
print(dilen(3,1))
print(add(3,0))
print(minus(3,4))
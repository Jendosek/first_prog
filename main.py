#1
class OddIterator:
    def __init__(self, name):
        self.name = name
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        if self.index < 0:
            raise ValueError("Bro 💀")
        value = self.name[self.index]
        self.index += 2
        return value
my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
my_iter = OddIterator(my_list)
for num in my_iter:
    print(num)
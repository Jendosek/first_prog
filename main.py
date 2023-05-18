#3
class ListIterator:
    def __init__(self, lst):
        self.data = lst
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
my_list = [1,2,3,4,5,6,7,8,9,10]
my_iter = ListIterator(my_list)
for num in my_list:
    print(num)
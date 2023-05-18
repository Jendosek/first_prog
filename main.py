#1
class OddIterator:
   def __init__(self, n):
       if not isinstance(n, int) or n <= 0:
           raise ValueError("треба n ціле натуральне число")
       self.n = n
       self.current = 1
   def __iter__(self):
        return self
   def __next__(self):
        if self.current > self.n:
            raise StopIteration
        else:
            result = self.current
            self.current +=2
            return result
#приклад використання
try:
    for num in OddIterator([1,2,3]):
        print(num)
except ValueError as e:
    print (e)
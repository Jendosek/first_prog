#1
class PrimeGenerator:
    def __init__(self):
        self.index = 2
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True
    def generate(self):
        new_index = self.index
        while True:
            if self.is_prime(new_index):
                self.index = new_index + 1
                return new_index
            new_index += 1

generator = PrimeGenerator()
for i in range(20):
    print(generator.generate())


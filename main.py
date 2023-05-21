#2
def average_closure():
    numbers = []
    def add_number(number):
        numbers.append(number)
    def get_average():
        print(numbers)
        return sum(numbers) / len(numbers)
    return add_number, get_average
add_number, get_average = average_closure()
add_number(1)
add_number(2)
add_number(3)
add_number(4)
add_number(5)
add_number(6)
add_number(7)
add_number(8)
add_number(9)
print(f"Середнє число зі списку: {get_average()}")


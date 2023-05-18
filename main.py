#2
my_list = [1,2,3,4,5,6,7,8,9]
class SquareGenerator:
    def __init__(self):
        if isinstance(my_list, list) is True:
            print(my_list)
        elif isinstance(my_list, list) is not True:
            TypeError("Brroo 💀")
    def my_generator(self, name):
        for num in my_list:
            num = num**2
            yield num
    for num in my_generator("", my_list):
        print(num)
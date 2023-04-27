#4
def squere(*args):
    dict_1 = []
    if not args:
        return None
    for value in args:
        if value % 2 != 0:
            dict_1.append(value)
    return dict_1
print("Список не праних чисел:")
print(squere(1,2,3,4,5,6,7,8,9,10,11))




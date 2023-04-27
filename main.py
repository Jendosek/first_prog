#3
def squere(**kwargs):
    dict_1 = {}
    if not kwargs:
        return None
    for key, value in kwargs.items():
        dict_1[key] = value ** 2
    return dict_1
print(squere(First = 1, Second = 2, Third = 3, Fourth = 4, Fifth = 5, Sixth = 6))


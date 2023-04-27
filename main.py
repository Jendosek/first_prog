#4
def func_4(*args):
    dict1 = {}
    for name, age in args:
        dict1[name] = age
    return dict1
print(func_4(*[('Женя', 16), ('Захар', 20), ('Влад', 15), ('Андре', 30)]))
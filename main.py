#4
def func_4(*args):
    dict1 = {}
    for name, age in args:
        dict1[name] = age
    return dict1
print(func_4(*[('Alice', 25), ('Bob', 30), ('Charlie', 35)]))

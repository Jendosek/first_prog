#2
print("У списку:")
lst = [i for i in range(1,10)]
print(lst)
def nums(*args):
    if not args:
        return None
    print(f"Мінімальне число: {min(args)}, Максимальне число: {max(args)}")
    return args
nums(1, 2, 3, 4, 5, 6, 7, 8 ,9)

#3
def cache(func):
    dict_1 = {}
    def wrapper(*args, **kwargs):
        if args in dict_1:
            return dict_1[args]
        else:
            res = func(*args)
            dict_1[args] = res
            return res, dict_1
    return wrapper
@cache
def example_function(x,y):
    return x * y
print(example_function(3,10))
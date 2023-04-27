#1
def string(*args):
    if not args:
        return None
    for argum in args:
        print(argum, end=", ")
    return args
string("Hello", "my", "new","programme")
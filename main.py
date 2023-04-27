#1
def string(*args):
    if not args:
        return None
    for arg in args:
        print(arg, end=", ")
    return args
string("Hello", "my", "new","programme")
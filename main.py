#1
def retur(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs) + 10
        print(x)
    return wrapper
@retur
def plus(n):
    return n
plus(13)
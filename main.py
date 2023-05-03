#2
def retur(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs) + 100
        print(x)
    return wrapper
@retur
def dobutok(x):
    res = 1
    for args in x:
        res *= args
    return res
lst = [1, 2, 3, 4, 5]
dobutok(lst)

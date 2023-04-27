#1
def func_1(*args):
    count = 0
    for argument in args:
        count += argument
        a = count / 5
    print(a)
func_1(2, 5, 6, 7, 13)

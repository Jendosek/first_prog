#1
import time
def timer(func):
    def wrapper(*args):
        res = func(args)
        for i in range(1,6):
            if 0 < i < 6:
                time.sleep(3)
                print(res)
        return res
    return wrapper
@timer
def example_fuck(x):
    return x
example_fuck("Hello World!")
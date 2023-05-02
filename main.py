#2
import time
def time_function(func):
    def wrapper (*args, **kwargs):
        stat_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        x = end_time - stat_time
        print("Час виконання функції:", round(x, 2), "секунд")
        return result
    return wrapper
@time_function
def example_function(x):
    time.sleep(2)
    return x
print(example_function("Hello World!"))
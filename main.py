#audit/work_2    ///    decorators
#1
def my_decorator(func):  #3
    def wrapper():  #4
        print("шо ти там")
        func()
        print("а ні шо")
    return wrapper
@my_decorator #2
def say_hello(): #1
    print("Hello!")
say_hello()

print()

#2
"""import time
def delay_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper
@delay_decorator
def sleepy():
    print("я сплю")
sleepy()

print()"""

#3
def cache_decorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper
@cache_decorator
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
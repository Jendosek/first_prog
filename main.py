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

#2


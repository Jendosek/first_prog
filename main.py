#1
def black_hole(*args):
    print(type(args))
    print(args)
    for argument in args:
        print(argument)
black_hole(234, "Earth", "russia", "time")

print()

#2
def black_hole_named(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
black_hole_named(name="Gleb", planet="Earth", food="Hleb", number = 5)

print()

#3
def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for argument in kwargs:
        print(argument)
black_hole_named(name="Gleb", planet="Earth", food="Hleb", number = 5)

print()

#4
def black_hole_full(*args, **kwargs):
    if not args:
        return 0  #для перевірки наявності не іменованих аргументів
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)
black_hole_full(234, "Earth", "russia", "time", 346, name="Gleb", planet="Earth", food="Hleb", number = 5)

print()

#5
def black_hole_full_2(var1, *args, **kwargs):
    if not args:
        return 0  #для перевірки наявності не іменованих аргументів
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)
black_hole_full_2(234, "Earth", "russia", "time", 346, name="Gleb", planet="Earth", food="Hleb", number = 5)
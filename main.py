#2
def max_lenth(*args):
    max_len = 0
    for arg in args:
        if len(arg) > max_len:
            max_len = len(arg)
    return print("Максимальна кількість символів у рядку:", max_len)
max_lenth("apple", "banana", "cat", "intereble", "Hello World")
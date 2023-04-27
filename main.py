#3

def sort(strings):
    return sorted(strings, key=len)
strings1 = input("Введіть рядок: ").split(' ')
strings1 = list(strings1)
x = sort(strings1)
print(x)j



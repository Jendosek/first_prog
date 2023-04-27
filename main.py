#1
a = 5
b = 10
def swap(a, b):
    a, b = b, a
    return a, b
print(f"До обміну: a = {a}, b = {b}")
a, b = swap(a, b)
print(f"Після обміну: a = {a}, b = {b}")


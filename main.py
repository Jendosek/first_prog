#2
def string(s):
    s = s.lower()
    s = s.replace(" ", "")  # Видаляємо всі пробіли з рядка
    if s == s[::-1]:
        print("True")
    else:
        print("False")
s1 = input("Введіть рядок: ")
string(s1)


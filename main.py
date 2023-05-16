#1
"""try:
    print("Start")
    print("error")
    print("Finish")
except:
    print("bro, it`s error💀💀💀")
print("let`s get it")"""

#2
"""def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry!, ми не можемо працювати з класом {type(var_1)} будь ласка введіть в str")
    else:
        return var_1
a = 1234
checker(a)
print()
print()"""

#3
class BuildingError(Exception):
    def __str__(self):
        return "шото багато"
def chech_material(amount, limit):
    if amount > limit:
        return "Достатньо матеріалів"
    else:
        raise BuildingError()
print(chech_material(123,300))
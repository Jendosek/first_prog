#2
def  count_vowels(s):
    vowels = 'aeiouyAEIOUY'
    count = 0
    for letters in s:
        if letters in vowels:
            count += 1
    return count
s1 = input("Введіть рядок: ")
print(count_vowels(s1))

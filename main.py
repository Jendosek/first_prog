strings = ['Hello', 'lol', 'Ololo lolo']
#s = input("Що перевірить")
def  count_vowels(s):
    vowels = 'eyuioaQEYUIOA'
    count = 0
    for letters in s:
        if letters in vowels:
            count += 1
    return count
for s in strings:
    print(f"У рядку {s} голосних літер {count_vowels(s)}")
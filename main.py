#4
def long_words(dictionary):
    return [word for word in dictionary if len(word) >= 5]
dict_1 = {'apple': 'a fruit', 'carrot': 'a vegetable', 'c++': 'programing language', 'bike': 'a vehicle'}
print(long_words(dict_1))

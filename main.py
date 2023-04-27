#5
def combine_dicts(*dicts):
    result_dict = {}
    for i in dicts:
        result_dict.update(i)
    return result_dict
print(combine_dicts({'apple': 'red', 'banana': 'blue', 'language': 'Ukrainian', "1": "2", "22":"2", "2":"9"}, {'apple': 'green', 'banana': 'yellow', "22":"3", 'cat': 'british', "1":"3", "33":"45"}, {'cat': 'turkish', "2":22, 'lanhuage': "English"}))

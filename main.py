#3
def loggging(func):
    def wrapper(t):
        result = func(t)
        print(f"Температура: {t} градусів Цельсія, становить {round(result)} градусів по Фаренгейту")
        return result
    return wrapper
@loggging
def example_func(t):
    return (t * 1.8) + 32
tempereture = 10
example_func(tempereture)

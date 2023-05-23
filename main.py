#3
import random
import logging

def last_task(file_path, num):
    try:
        with open(file_path, 'w') as file:
            for i in range(num):
                rad = random.randint(1,100)
                file.write(str(rad) + '\n')
                logging.info(f"Рандомне число: {rad}")
    except Exception as e:
        logging.error(f"error: {e}")
file_path = "input_random.txt"
last_task("input_random.txt",  input("Кількість генерованих чисел: "))
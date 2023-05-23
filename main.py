#2
import logging

logger = ''
print("Щоб вийти з програми натисніть q")
while logger != "q":
    logger = input("Введіть текст (без чисел): ")
    logging.basicConfig(level=logging.INFO,
                    filename= "logss.log",
                    filemode= 'w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"інфформація {logger} була додана до файлу")
    for i in logger:
        if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            logging.error(f"число ({i}) вводити неможна")
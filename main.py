import logging  #стандартна бібліотека для логування програм
logging.basicConfig(level=logging.DEBUG,
                    filename= "logs.log",
                    filemode= 'w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")
try:
    print(10/0)
except Exception:
    logging.exception("na 0 dilitu ne mogna")
import logging


def factorial(n):
    logging.info(f"Розпочато обччислення факторіалу числа {n}")
    result = 1
    for i in range(1, n + 1):
        result *= i
    logging.info(f"Обччислення факторіалу числа {n} завершено. Резуультат {result}")
    return result
logging.basicConfig(level=logging.INFO)
factorial(5)
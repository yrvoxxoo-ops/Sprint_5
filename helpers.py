import random
import time


def generate_email():
    random_number = random.randint(100, 999)
    timestamp = int(time.time())

    return f"aida_samarkina_42_{random_number}_{timestamp}@yandex.ru"
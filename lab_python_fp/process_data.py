import json
import sys
from unique import Unique
from gen_random import gen_random
from print_result import print_result
from cm_timer import cm_timer_1

# Получаем путь к файлу из аргументов командной строки
path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Функция f1: отсортированный список профессий без повторений (игнорируя регистр)
@print_result
def f1(arg):
    return sorted(Unique([item['profession'] for item in arg], ignore_case=True), key=lambda x: x.lower())

# Функция f2: фильтрация элементов, начинающихся со слова "программист"
@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

# Функция f3: добавление строки "с опытом Python" к каждой профессии
@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

# Функция f4: добавление зарплаты к каждой специальности
@print_result
def f4(arg):
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f'{profession}, зарплата {salary} руб.' for profession, salary in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

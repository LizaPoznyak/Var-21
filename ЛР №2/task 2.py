# Напишите функцию, которая будет принимать один аргумент.
# Если в функцию передаётся список, Найдите сумму элементов между двумя первыми нулями.
# Если кортеж, найти максимальный и минимальный элементы. Поменять их местами.
# Число – найти сумму четных цифр.
# Строка – каждый символ перевести в соответствующий ему код из таблицы символов Unicode.
# Сделать проверку со всеми этими случаями.

import random


def func(arg):
    if isinstance(arg,
                  list):  # Возвращает True, если указанный объект является экземпляром указанного класса (классов), либо наследующегося от него класса
        indexes = [i for i, value in enumerate(arg) if value == 0][:2]
        if len(indexes) == 0:
            return "В списке нет нулей!"
        elif len(indexes) == 1:
            return "В списке есть только один ноль!"
        elif len(arg[indexes[0] + 1:indexes[1]]) == 0:
            return "Суммы нет! Между нулями нет элементов!"
        else:
            summ = sum(arg[indexes[0] + 1:indexes[1]])  # 1:indexes[1] срез до второго нуля
            return summ
    elif isinstance(arg, tuple):
        max_value = max(arg)
        min_value = min(arg)
        new_tuple = tuple(
            [min_value if value == max_value else max_value if value == min_value else value for value in arg])
        return new_tuple
    elif isinstance(arg, int):
        digit_sum = sum([int(digit) for digit in str(arg) if int(digit) % 2 == 0])
        return digit_sum
    elif isinstance(arg, str):
        unicode_list = [ord(char) for char in
                        arg]  # ord(char) возвращает числовое представление символа char в таблице символов Unicode
        return unicode_list
    else:
        return "Неизвестный тип!"


def fill_list(my_list, length_of_my_list):
    numberToAdd = 0
    print("Введите элементы списка:")
    for i in range(1, length_of_my_list + 1):
        print("Элемент №", i)
        while True:
            try:
                numberToAdd = int(input())
            except Exception:
                print("Некорректный ввод!")
                continue
            break
        my_list.append(numberToAdd)
    return my_list


while True:
    choice = input("Выберите желаемый тип:\n1 - Список\n2 - Кортеж\n3 - Число\n4 - Строка\n5 - Выйти\n")
    if choice == "1":
        while True:
            try:
                length = int(input("Введите размер списка: "))
            except Exception:
                print("Некорректный ввод!")
                continue
            if length <= 0:
                print("Некорректный ввод!")
                continue
            while True:
                choice = input("Выберите способ заполнение списка:\n"
                               "1 - Заполнить список случайными числами\n"
                               "2 - Заполнить список числами, введенными с клавиатуры\n")
                if choice == "1":
                    listOfNumbers = [random.randint(0, 100) for i in range(length)]
                elif choice == "2":
                    listOfNumbers = []
                    listOfNumbers = fill_list(listOfNumbers, length)
                else:
                    print("Такого варианта выбора нет!")
                    continue
                break
            print("Список: ", listOfNumbers)
            print("Сумма элементов между двумя первыми нулями: ", func(listOfNumbers))
            break
    elif choice == "2":
        while True:
            try:
                length = int(input("Введите размер кортежа: "))
            except Exception:
                print("Некорректный ввод!")
                continue
            if length <= 0:
                print("Некорректный ввод!")
                continue
            tupleOfNumbers = tuple(random.randint(0, 100) for i in range(length))
            print("Кортеж: ", tupleOfNumbers)
            print("Ответ (поменять местами min и max элементы):", func(tupleOfNumbers))
            break
    elif choice == "3":
        while True:
            try:
                digit = int(input("Введите число: "))
            except Exception:
                print("Некорректный ввод!")
                continue
            print("Сумма четных цифр: ", func(digit))
            break
    elif choice == "4":
        string = input("Введите строку: ")
        print("Ответ (каждый символ перевести в соответствующий ему код из таблицы символов Unicode): ", func(string))
    elif choice == "5":
        break
    else:
        print("Такого варинта выбора нет!")

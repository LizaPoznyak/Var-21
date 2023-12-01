# Найти в матрице первую строку, все элементы которой упорядочены по возрастанию. Изменить упорядоченность элементов
# этой строки на обратную.

import random


def fill_random_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            random_number = random.randint(1, 100)
            row.append(random_number)
        matrix.append(row)
    return matrix


def fill_matrix(rows, columns):
    matrix = []
    number = 1
    print("Введите элементы матрицы:")
    for _ in range(rows):
        row = []
        for _ in range(columns):
            while True:
                try:
                    numberToAdd = int(input("Элемент №" + str(number) + "\n"))
                except Exception:
                    print("Некорректный ввод!")
                    continue
                number += 1
                break
            row.append(numberToAdd)
        matrix.append(row)
    return matrix


def out_print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()


def find_ordered_row(matrix):
    for row in matrix:
        is_ordered = all(row[i] <= row[i + 1] for i in range(len(row) - 1))
        if is_ordered:
            return row
    return None


while True:
    try:
        number_of_rows = int(input("Введите количество строк: "))
        number_of_columns = int(input("Введите количество столбцов: "))
    except Exception:
        print("Некорректный ввод!")
        continue
    if number_of_rows <= 0 or number_of_columns <= 0:
        print("Некорректный ввод!")
        continue
    while True:
        choice = input("Выберите способ заполнение матрицы:\n"
                       "1 - Заполнить матрицу случайными числами\n"
                       "2 - Заполнить матрицу числами, введенными с клавиатуры\n")
        if choice == "1":
            matrix = fill_random_matrix(number_of_rows, number_of_columns)
        elif choice == "2":
            matrix = fill_matrix(number_of_rows, number_of_columns)
        else:
            print("Такого варианта выбора нет!")
            continue
        break
    out_print_matrix(matrix)
    ordered_row = find_ordered_row(matrix)
    if ordered_row:
        reversed_row = ordered_row[::-1]
        print("Упорядоченная строка: ", reversed_row)
    else:
        print("Упорядоченная строка не найдена!")
    break

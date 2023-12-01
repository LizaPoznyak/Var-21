while True:
    ch = ','
    string = input("Введите последовательность чисел, разделённых запятой :\n")
    if all((w.isdigit() or w == ch) for w in string):
        listOfNumbers = string.split(',')
        break
    else:
        print("Некорректный ввод!")
        continue
tupleOfNumbers = tuple(listOfNumbers)
print("Список : ", listOfNumbers, "\nКортеж : ", tupleOfNumbers)
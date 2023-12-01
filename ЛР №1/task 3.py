import random

while True:
    try:
        length = int(input("Введите размер списка : "))
    except Exception:
        print("Некорректный ввод!")
        continue
    length = int(length)
    if length <= 0:
        print("Некорректный ввод!")
        continue
    listOfNumbers = []
    listOfEvenNumbers = []
    while True:
        choice = input("Выберите способ заполнение списка :\n"
                       "1 - Заполнить список случайными числами\n"
                       "2 - Заполнить список числами, введенными с клавиатуры\n")
        if choice == "1":
            listOfNumbers = [random.randint(0, 100) for i in range(length)]
        elif choice == "2":
            numberToAdd = 0
            print("Введите элементы списка :")
            for i in range(1, length + 1):
                print("Элемент №", i)
                while True:
                    try:
                        numberToAdd = int(input())
                    except Exception:
                        print("Некорректный ввод!")
                        continue
                    break
                listOfNumbers.append(numberToAdd)
        else:
            print("Такого варианта выбора нет!")
            continue
        break
    listOfNumbers.sort(reverse=True)
    print("Ваш список :\n", listOfNumbers)
    for i in range(1, length + 1):
        if listOfNumbers[i - 1] % 2 == 0:
            listOfEvenNumbers.append(listOfNumbers[i - 1])
    if len(listOfEvenNumbers) == 0:
        print(listOfNumbers[0])
    else:
        maxEvenNumber = listOfEvenNumbers[0]
        for i in range(1, len(listOfEvenNumbers) + 1):
            if listOfEvenNumbers[i - 1] > maxEvenNumber:
                maxEvenNumber = listOfEvenNumbers[i]
        print("Наибольший чётный элемент списка :\n", maxEvenNumber)
    break
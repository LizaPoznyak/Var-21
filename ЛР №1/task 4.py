my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
keysWithMinValue = []
i = 0
while i != 3:
    minKey = min(my_dict, key=my_dict.get) # Нахождение ключа с минимальным значением с использованием функции min()
    keysWithMinValue.append(minKey)
    del my_dict[minKey]
    i += 1
print(keysWithMinValue)
# метод get возвращает найденное значение в словаре по ключу
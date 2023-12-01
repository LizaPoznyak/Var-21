amount = 0
string = input("Введите строку : ")
listOfWords = string.split(' ')
maxLenWord = listOfWords[0]
for i in range(1, len(listOfWords)):
    if listOfWords[i - 1] > maxLenWord:
        maxLenWord = listOfWords[i - 1]
    if len(listOfWords[i - 1]) % 2 == 0:
        amount += 1
    else:
        continue
print("Количество слов чётной длины : ", amount)
print("Самое длинное слово : " + maxLenWord)
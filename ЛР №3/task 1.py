# Создать программный файл F1 в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка. Создать текстовый файл F1 не менее,
# чем из 10 строк и записать в него информацию. Скопировать в файл F2 только строки из F1, которые не содержат цифр.

with open('F1.txt', 'w', encoding='utf-8') as f1:
    print("Введите строку (для завершения введите пустую строку):\n")
    while True:
        line = input()
        if line == "":
            break
        f1.write(line + "\n")

with open('F1.txt', 'r', encoding='utf-8') as f1:
    lines = f1.readlines()

with open('F2.txt', 'w', encoding='utf-8') as f2:
    for line in lines:
        if not any(c.isdigit() for c in line):
            f2.write(line)

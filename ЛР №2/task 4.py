# Напишите программу, демонстрирующую работу try\except\finally.

file = None
try:
    file = open("my_file.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Файл не найден!")
finally:
    if file:
        file.close()

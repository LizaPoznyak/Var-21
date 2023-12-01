# Написать функцию для определения всех чисел, на которые без остатка делится указанное число.

def func(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


while True:
    try:
        digit = int(input("Введите число: "))
        if digit > 0:
            print("Все делители числа:\n", func(digit))
            break
        else:
            print("Число равно нулю!")
    except Exception:
        print("Некорректный ввод!")

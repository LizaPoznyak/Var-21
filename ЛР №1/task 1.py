while True:
    try:
        digit = int(input("Введите число : "))
        if digit > 0:
            divisors = []
            for i in range(1, digit + 1):
                if digit % i == 0:
                    divisors.append(i)
            print("Все делители числа :\n", divisors)
            break
        else:
            print("Число равно нулю!")
    except Exception:
        print("Некорректный ввод!")
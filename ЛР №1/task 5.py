def add_in_cart(name):
    productNames[name] = [catalog[name][0], catalog[name][1], catalog[name][2]]
    while True:
        try:
            amount = int(input("Введите количество изделий, которое вы хотите приобрести :\n"))
            if amount <= 0:
                print("Количество не может быть отрицательно или равно нулю!")
            elif amount <= catalog[name][2]:
                productNames[name][2] = amount
                catalog[name][2] -= amount
                break
            else:
                print("Неверное количество!")
        except Exception:
            print("Некорректный ввод!")


def del_from_cart():
    check = False
    name = input("Введите название изделия, которое вы хотите удалить :\n")
    name = name.capitalize()
    for key in productNames:
        if name == key:
            catalog[key][2] += productNames[key][2]
            productNames.pop(key)
            check = True
            break
    if not check:
        print("Такого изделия нет в корзине!")


def get_total_price():
    totalPrice = 0.0
    for key in productNames:
        totalPrice += productNames[key][1] * productNames[key][2]
    return totalPrice


def receipt():
    for key in productNames:
        print("{:.<{}}".format(key + " * " + str(productNames[key][2]), 20),
              "{:.>{}}".format(str('%.2f' % (productNames[key][1] * productNames[key][2])) + " BYN", 11))
    print("{:.<{}}".format("Итого :", 20),
          "{:.>{}}".format('%.2f' % get_total_price() + " BYN", 11))


def purchase():
    choice = ""
    while choice != "6":
        print("\t\tМеню покупки\n"
              "1 - Добавить изделие в корзину\n"
              "2 - Удалить изделие из корзины\n"
              "3 - Просмотр изделий в корзине\n"
              "4 - Посчитать общую стоимость изделий в корзине\n"
              "5 - Оплатить\n"
              "6 - Вернуться назад")
        choice = input()
        if choice == "1":
            name = input("Введите название изделия, которое вы хотите приобрести :\n")
            name = name.capitalize()
            if name not in catalog.keys():
                print("Такого изделия нет!")
                continue
            if name in productNames.keys():
                print("Такое изделие уже есть в корзине!")
                continue
            if catalog[name][2] == 0:
                print("Данного товара нет в наличии!")
                continue
            add_in_cart(name)
        elif choice == "2":
            if len(productNames) == 0:
                print("В корзине нет изделий!")
            else:
                del_from_cart()
        elif choice == "3":
            if len(productNames) == 0:
                print("В корзине нет изделий!")
            else:
                for key in productNames:
                    print(key, " - ", productNames[key][0], ", ", productNames[key][1], " BYN, ",
                          productNames[key][2], " шт.")
        elif choice == "4":
            if len(productNames) == 0:
                print("В корзине нет изделий!")
            else:
                print("Общая стоимость изделий в корзине : ", '%.2f' % get_total_price())
        elif choice == "5":
            if len(productNames) == 0:
                print("В корзине нет изделий!")
            else:
                receipt()
                productNames.clear()


print("\t\tЮвелирный магазин")
catalog = {"Кольцо": ["Серебро", 49.20, 15], "Серьги": ["Золото", 367.10, 6],
           "Браслет": ["Белое золото", 695.02, 3]}
productNames = {}
mainChoice = ""
while mainChoice != "6":
    print("1. Просмотр описания : название - описание\n"
          "2. Просмотр цены : название - цена\n"
          "3. Просмотр количества : название - количество\n"
          "4. Всю информацию\n"
          "5. Покупка\n"
          "6. До свидания")
    mainChoice = input()
    if mainChoice == "1":
        if len(catalog) == 0:
            print("Список изделий пуст!")
        else:
            for key in catalog:
                print(key, " - ", catalog[key][0])
    elif mainChoice == "2":
        if len(catalog) == 0:
            print("Список изделий пуст!")
        else:
            for key in catalog:
                print(key, " - ", catalog[key][1], " BYN")
    elif mainChoice == "3":
        if len(catalog) == 0:
            print("Список изделий пуст!")
        else:
            for key in catalog:
                print(key, " - ", catalog[key][2], " шт.")
    elif mainChoice == "4":
        if len(catalog) == 0:
            print("Список изделий пуст!")
        else:
            for key in catalog:
                print(key, " - ", catalog[key][0], ", ", catalog[key][1], " BYN, ",
                      catalog[key][2], " шт.")
    elif mainChoice == "5":
        purchase()
    elif mainChoice == "6":
        print("До свидания!")
    else:
        print("Такого варианта выбора нет!")
        continue

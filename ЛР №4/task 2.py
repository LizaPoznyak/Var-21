# Создать класс Employee (сотрудник) с полями ФИО, стаж, часовая
# заработная плата, количество отработанных часов, оклад, премия. Создать
# список сотрудников компании. Реализовать ввод данных всех сотрудников с
# клавиатуры. Рассчитать с помощью методов класса заработную плату за
# отработанное время, и премию, размер которой определяется в зависимости
# от стажа работника (при стаже до 1 года 1%, до 3 лет 5%, до 5 лет 8%, свыше
# 5 лет 15%). С помощью метода печати, реализовать вывод информации о
# работнике на экран.
class Employee:
    def __init__(self, FIO, experience, hour_rate, hours_worked, salary, bonus):
        self.FIO = FIO
        self.experience = experience
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked

    def calculate_bonus(self):
        if self.experience < 1:
            return self.salary * 0.01
        elif self.experience < 3:
            return self.salary * 0.05
        elif self.experience < 5:
            return self.salary * 0.08
        else:
            return self.salary * 0.15

    def print_info(self):
        print("\n\t---Информация о ", self.FIO, "---\nСтаж : ", self.experience, " лет", "\nЧасовая ставка : ",
              self.hour_rate, "\nОтработанные часы : ", self.hours_worked, "\nЗарплата : ",
              self.salary, "\nПремия : ", self.bonus)


employee_list = []
while True:
    try:
        num_employees = int(input("Введите количество сотрудников : "))
        if num_employees <= 0:
            print("Количество не может быть отрицательно или равно нулю!")
        else:
            break
    except:
        print("Некорректный ввод!")
for i in range(num_employees):
    print("\nВведите данные сотрудника №", i + 1)
    while True:
        FIO = input("Введите ФИО сотрудника : ")
        if FIO:
            break
    while True:
        try:
            experience = int(input("Введите опыт сотрудника (в годах) : "))
            if experience <= 0:
                print("Опыт не может быть отрицательный или равен нулю!")
            else:
                break
        except:
            print("Некорректный ввод!")
    while True:
        try:
            hour_rate = float(input("Введите часовую ставку сотрудника : "))
            if hour_rate <= 0:
                print("Часовая ставка не может быть отрицательна или равна нулю!")
            else:
                break
        except:
            print("Некорректный ввод!")
    while True:
        try:
            hours_worked = int(input("Введите количество отработанных часов : "))
            if hours_worked <= 0:
                print("Количество отработанных часов не может быть отрицательным или равно нулю!")
            else:
                break
        except:
            print("Некорректный ввод!")
    employee_list.append(Employee(FIO, experience, hour_rate, hours_worked, 0, 0))
for employee in employee_list:
    employee.salary = employee.calculate_salary()
    employee.bonus = employee.calculate_bonus()
    employee.print_info()

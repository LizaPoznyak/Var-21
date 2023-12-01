# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад более 2 тысяч, вывести фамилии этих сотрудников.
# Вывести на экран сотрудников с минимальным окладом.

with open('employees.txt', 'r', encoding='utf-8') as f:
    high_salary_employees = []
    lines = f.readlines()
    for line in lines:
        surname, salary = line.split()
        salary = int(salary)
        if salary > 2000:
            high_salary_employees.append(surname)
    print("Сотрудники с окладом более 2000:")
    for surname in high_salary_employees:
        print(surname)
    min_salary_employees = []
    min_salary = min([int(line.split()[1]) for line in lines])
    for line in lines:
        if int(line.split()[1]) == min_salary:
            min_salary_employees.append(line.split()[0])
    print("\nСотрудники с минимальным окладом:")
    for surname in min_salary_employees:
        print(surname)

# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

with open("companies.txt", "r", encoding='utf-8') as file:
    companies = file.readlines()

profits = []
total_profit = 0

for company in companies:
    data = company.split(" ")
    name = data[0]
    revenue = int(data[2])
    expenses = int(data[3])
    profit = revenue - expenses
    if profit > 0:
        profits.append({name: profit})
        total_profit += profit
    else:
        profits.append({name: "Убыток"})

average_profit = total_profit / len(profits)

result = [profits, {"Средняя прибыль": average_profit}]

with open("result.json", "w", encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False)

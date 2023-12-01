import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# №1 и №2
test = pd.read_csv("test.csv", nrows=1000)

# №3
check = test.isnull().sum()
print(check)

test2 = test.fillna("unknown")

# №4
x = 1
for column_name in test.columns:
    new_series_array = np.array(test[column_name])
    plt.subplots_adjust(hspace=0.5)
    plt.hist(new_series_array)
    plt.title(column_name)
    x += 1
plt.show()

x = 1
for column_name in test.columns:
    new_series_array = np.array(test[column_name])
    plt.subplot(4, 5, x)
    plt.subplots_adjust(hspace=0.5)
    plt.hist(new_series_array)
    plt.yscale(value="log")
    plt.title(column_name)
    x += 1
plt.show()

# №5
x = 10
for values in test2["LifeSquare"]:
    if x > 80:
        x = 15
    if values != "unknown":
        if type(values) == float:
            test2 = test2.replace(values, x)
    x += 1
for values in test2["Square"]:
    if x > 150:
        x = 15
    if values != "unknown":
        if type(values) == float:
            test2 = test2.replace(values, x)
    x += 1
for values in test2["KitchenSquare"]:
    if x > 50:
        x = 15
    if values != "unknown":
        if type(values) == float:
            test2 = test2.replace(values, x)
    x += 1
for values in test2["Floor"]:
    if x > 25:
        x = 10
    if values != "unknown":
        if int(values) <= 0 or int(values) > 25:
            test2 = test2.replace(values, x)
    x += 1
for values in test2["HouseFloor"]:
    if x > 25:
        x = 10
    if values != "unknown":
        if int(values) <= 0 or int(values) > 25:
            test2 = test2.replace(values, x)
    x += 1
for values in test2["HouseYear"]:
    if x > 2023:
        x = 1990
    if values != "unknown":
        if values < 1976 or values > 2023:
            test2 = test2.replace(values, x)
    x += 1

# №6
rooms_num = pd.DataFrame(test.groupby(test["Rooms"].tolist(), as_index=False).size())
rooms_num.columns = ["Количество комнат", "Количество квартир с таким же количеством комнат"]
print(rooms_num)

# №7
districts_info = pd.pivot_table(test, index=["DistrictId"], columns=["Rooms"], values=["LifeSquare"])
print(districts_info.fillna("unknown"))

# №8
test2.to_csv("Позняк.csv")

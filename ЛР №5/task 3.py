import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# №1
Fun_x = np.array([0])
x = 3.67
a = 0
while a <= 2:
    f = np.exp(a * x) - 3.45 * a
    Fun_x = np.append(Fun_x, f)
    a += 0.2
X = np.arange(0, 2, 0.2)
Fun_x = np.delete(Fun_x, 0)
if len(X) != len(Fun_x):
    min_len = min(len(X), len(Fun_x))
    X = X[:min_len]
    Fun_x = Fun_x[:min_len]
Res = pd.DataFrame({"a": X, "f(t)": Fun_x})
print(Res)
print("Наибольшее значение - {}".format(Fun_x.max()))
print("Наименьшее значение - {}".format(Fun_x.min()))
print("Среднее значение - {}".format(Fun_x.mean()))
print("Количество элементов массива значений функции f(a) - {}".format(Fun_x.size))
print("Отсортированный по убыванию numpy-массив функций f(a)\n", np.sort(Fun_x, axis=-1))
plt.plot(X, Fun_x, label="0 <= a <= 2; 1 <= f(a) < 734")
plt.axhline(y=Fun_x.mean(), color="green", label="среднее значение f(a)")
plt.title("График изменения значений функции f(a)")
plt.xlabel("Значение аргумента a")
plt.ylabel("Значение функции f(a)")
plt.legend(loc="upper right", frameon=False)
plt.show()

# №2
u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.cos(v) * np.sin(u)
z1 = x ** 0.25 + y ** 0.25
z2 = x ** 2 - y ** 2
z3 = 2 * x + 3 * y
z4 = x ** 2 + y ** 2
z5 = 2 + 2 * x + 2 * y - x ** 2 - y ** 2
fig = plt.figure()
ax = fig.add_subplot(2, 2, 1, projection='3d')
ax.plot_surface(x, y, z1)
ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.plot_wireframe(x, y, z2)
ax = fig.add_subplot(2, 2, 3, projection='3d')
ax.plot_wireframe(x, y, z3)
ax = fig.add_subplot(2, 2, 4, projection='3d')
ax.scatter(x, y, z4)
ax = fig.add_subplot(2, 1, 1, projection='3d')
ax.plot_surface(x, y, z5)
plt.show()

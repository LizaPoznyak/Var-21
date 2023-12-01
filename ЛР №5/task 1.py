import numpy as np

a = 1.21
b = 0.371
f1 = np.array([np.tan((a + b) ** 2)])
f2 = np.array([(a + 1.5) ** (1 / 3)])
f3 = np.array([a * (b ** 5)])
f4 = np.array([b / np.log(a ** 2)])
result = f1 - f2 + f3 - f4
print("№1.1\n", result)

X_column1 = np.ones((12, 1))
X_column2 = np.random.randint(21, 33, (12, 1))
X_column3 = np.random.randint(60, 82, (12, 1))
X = np.hstack((X_column1, X_column2, X_column3))
Y = np.random.uniform(13.5, 18.6, (12, 1))
A = np.linalg.inv((X.transpose().dot(X))).dot(X.transpose().dot(Y))
print("\n№1.2\n", A)

Y_check = A[0] + A[1] * X_column2 + A[2] * X_column3
print("\nПроверка :\n", Y_check)

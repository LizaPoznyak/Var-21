# Класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первый метод: создайте переменную и выведите её.
# Второй метод: верните сумму 2-ух глобальных переменных.
# Третий метод: верните результат возведения первой динамической
# переменной во вторую динамическую переменную.
# Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a.
class Example:
    # Статические поля (переменные класса)
    a = 5  # default_a = 5
    b = 10

    def __init__(self, c, d):  # метод-конструктор
        # динамические поля (переменные объекта)
        self.c = c  # self - ссылка на экземпляр класса
        self.d = d

    def print_variable(self):
        print(self.c)

    def sum_variables(self):
        return self.a + self.b

    def pow_variables(self):
        return self.c ** self.d


obj = Example(3, 2)
obj.print_variable()
print(obj.sum_variables())
print(obj.pow_variables())
print(obj.a)

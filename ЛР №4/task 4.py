# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса
class Car:
    # метод экземпляра класса
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    # метод экземпляра класса
    def display_info(self):
        print(f"\nИнформация о машине :\nЦвет : {self.color}\nМарка : {self.brand}\nМодель : {self.model}")

    @staticmethod
    def honk():
        print("Бип-бип!")

    @classmethod
    def input_car_info(cls):
        while True:
            brand = input("Введите марку машины : ")
            if brand:
                break
        while True:
            model = input("Введите модель машины : ")
            if model:
                break
        while True:
            color = input("Введите цвет машины : ")
            if color:
                break
        return cls(brand, model, color)


car = Car.input_car_info()
car.display_info()
Car.honk()

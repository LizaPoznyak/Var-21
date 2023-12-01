# Создать классы «Зоомагазин», «Животное», «Рыбы», «Птицы». Определить
# свойства: породу и стоимость для указанных животных (рыб, птиц), в
# каждом классе реализовать переопределение метода «способ передвижения».
# Вывести данные о самой дорогой породе. Предусмотреть метод записи
# информации в файл Python
class ZooShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_most_expensive_breed(self):
        most_expensive_breed = None
        max_price = 0
        for animal in self.animals:
            if animal.price > max_price:
                max_price = animal.price
                most_expensive_breed = animal.breed
        return most_expensive_breed

    def write_info_to_file(self, file_name):
        with open(file_name, 'w') as file:
            for animal in self.animals:
                file.write(f"Порода : {animal.breed}, Цена : {animal.price}\n")


class Animal:
    def __init__(self, breed, price):
        self.breed = breed
        self.price = price

    def move(self):
        pass

class Fish(Animal):
    def move(self):
        return "Плавает"

class Bird(Animal):
    def move(self):
        return "Летает"


zoo_shop = ZooShop()
zoo_shop.add_animal(Fish("Золотая рыбка", 10))
zoo_shop.add_animal(Fish("Рыба-клоун", 15))
zoo_shop.add_animal(Bird("Попугай", 20))
zoo_shop.add_animal(Bird("Канарейка", 25))
print("Самая дорогая порода : ", zoo_shop.get_most_expensive_breed())
zoo_shop.write_info_to_file("animals.txt")

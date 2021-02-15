# Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.

class Auto:
    def __init__(self, brand, model, years, doors, price):
        self.brand = brand
        self.__model = model
        self.__year = years
        self.__doors = doors
        self.price = price

    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def years(self):
        return self.years

    @years.setter
    def years(self, years):
        self.__year = years

    @property
    def doors(self):
        return self.doors

    @doors.setter
    def doors(self, doors):
        self.__doors = doors

    def move(self):
        print('The car is moving now\n')
    def beep(self):
        print('The car beeps to others\n')

car_defolt = Auto('brand: none', 'model: none', 'year: none', 'doors: none' , 'price: none')

print(car_defolt.brand)

car_defolt.move()
car_defolt.beep()

car_defolt.brand = 'BMW'
car_defolt.set_years = '2003'
car_defolt.set_doors = '3 doors'

print(car_defolt.brand)
print(car_defolt.get_years)
print(car_defolt.get_doors)
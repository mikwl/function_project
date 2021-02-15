# class Dog:
#     pass
#
# dog = Dog()
# labrador = Dog()
#
# print(dog, labrador)

# class Dog:
#     def bark(self):
#         print('Woof Woof!')
#     def jump(self):
#         print('Jump!')
#     def run(self):
#         print('Run!')
#
# dog_1 = Dog()
# dog_1.bark()
# dog_1.jump()
# dog_1.run()

# КОНСТРУКТОР

# class Dog:
#     def __init__(self, name):
#         self.name = name
#
# # self - ССЫЛКА. ЧТОБЫ ПОЛУЧИТЬ ДОСТУП К НЭЙМУ МЫ ДОЛЖНЫ ПИСАТЬ СЕЛФ.
#
# dog_1 = Dog('Bob')
# print(dog_1.name)
#
# dog_2 = Dog('Max')
# print(dog_2.name)
#
# dog_3 = Dog('David sexy')
# print(dog_3.name)

# СОЗДАТЬ КЛАСС DOG . КЛАСС ИМЕЕТ 4 АТРИБУТА: HEIGHT, WEIGHT, NAME, AGE.
# КЛАСС ИМЕЕТ ТРИ МЕТОДА: JUMP RUN WALK
# КАЖДЫЙМЕТОД ВЫВОДИТ СООБЩЕНИЕ НА ЭКРАН. СОЗДАТЬ ОБХЕКТ КЛАССА ДОГ, ВЫЗВАТЬ ВСЕ МЕТОДЫ ОБЪЕКТА И ВЫВЕСТИ НА ЭКРАН
# ВСЕ ЕГО АТРИБУТЫ

# class Dog:
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#     def cnange_height(self, height):
#         self.height = height
#     def jump(self):
#         print('Jump!')
#     def run(self):
#         print('Run!')
#     def walk(self):
#         print('Walk!')
#
#
# dog_1 = Dog('Height: 100 cm', 'Weight: 12 kg', 'Name: Marley', 'Age: 7 years')
#
# print(dog_1.height)
# print(dog_1.weight)
# print(dog_1.name)
# print(dog_1.age)
#
# dog_1.run()
# dog_1.jump()
# dog_1.walk()
#
# dog_1.cnange_height('Height: 120 cm')
#
# print(dog_1.height)

# задание 11. 05

# class Dog:
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#     def cnange_height(self, height):
#         self.height = height
#     def change_name(self, name):
#         self.name = name
#     def jump(self):
#         print('Jump!')
#     def run(self):
#         print('Run!')
#     def walk(self):
#         print('Walk!')
#
#
# dog_1 = Dog('Height: 100 cm', 'Weight: 12 kg', 'Name: Marley', 'Age: 7 years')
#
# print(dog_1.height)
# print(dog_1.weight)
# print(dog_1.name)
# print(dog_1.age)
#
# dog_1.run()
# dog_1.jump()
# dog_1.walk()
#
# dog_1.cnange_height('Height: 120 cm')
# dog_1.change_name('Name: Bob Marley')
#
# print(dog_1.height)
# print(dog_1.name)


# МОДИФИКАТОРЫ ДОСТУПА

# class Dog:
#     def __init__(self, name, age, weight):
#         self.__name = name
#         self._age = age
#         self.weight = weight
#
# dog = Dog('Name: Bob', 8, 2.4)
# # print(dog.__name) - ВЫДАСТ ОШИБКУ
# print(dog._Dog__name)
# print(dog._age)
# print(dog.weight)
#
# class Dog:
#     def __init__(self, height, weight, name, age, master):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#         self.__master = master
#     def get_master(self):
#         return self.__master
#
# dog_1 = Dog('Height: 100 cm', 'Weight: 12 kg', 'Name: Marley', 'Age: 7 years', 'Master')
#
# print(dog_1.get_master())

# print(dog_1._Dog__master) он вывел только из-за того, что я ЗНАЛ, что есть такой класс как Мастер и он скрытый

# class Dog:
#     def __init__(self, master):
#         self.__master = master
#     def get_master(self):
#         return self.__master
#     def set_master(self, master):
#         self.__master = master
#
# dog = Dog('Alex')
# print(dog.get_master())
#
# dog.set_master('Pavel')
# print(dog.get_master())

# class Dog:
#     def __init__(self, name, age, height, weight, master):
#         self.__name = name  # private
#         self._age = age  # protected
#         self.height = height  # public
#         self.weight = weight
#         self.__master = master
#         self.__address = 'Minsk'
#
#
#     def get_address(self):
#         return self.__address
#     def set_address(self, address):
#         self.__address = address
#
# corgi = Dog('Pinky', 3, 50, 4, 'Master')
#
# print(corgi.get_address())

# class Dog:
#     def __init__(self, master):
#         self.__master = master
#     @property
#     def master(self):
#         return self.__master
#     @master.setter
#     def master(self, master):
#         if len(master) < 5:
#             self.__master = master
#
# dog = Dog('Alex')
#
# dog.master = 'Moe'
# print(dog.master)

# class Dog:
#     def __init__(self, name, age, weight):
#         self.__name = name
#         self.__age = age
#         self.__weight = weight
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.__weight = weight
#
#
# dog = Dog('Alex', 9, 25)
#
# print(dog.name, dog.age, dog.weight)
#
# dog.name = 'Leo'
# dog.age = 1
# dog.weight = 10
#
# print(dog.name, dog.age, dog.weight)

# ЗАДАНИЕ 11.09
# СОЗЗАТЬ ТРИ КЛАССА. DOG CAT PARROT. атрибуты КАЖЛОГО КЛАССА: NAME, AGE, MASTER.
# каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep
# класс Parrot имеет дополнительной метод fly.
# Cat - meow, Dog - bark.

# class Dog:
#     def __init__(self, name, age, master):
#         self.__name = name
#         self.__age = age
#         self.__master = master
#
#     def run(self):
#         print('Run!')
#
#     def jump(self):
#         print('Jump!')
#
#     def birthday(self):
#         a = int(age) + 1
#
#         @property
#         def name(self):
#             return self.name
#
#         @name.setter
#         def name(self, name):
#             self.__name = name
#
#         @property
#         def age(self):
#             return self.age
#
#         @age.setter
#         def age(self, age):
#             self.__age = age
#
#         @property
#         def master(self):
#             return self.age
#
#         @master.setter
#         def master(self, master):
#             self.__master = master
#
#
# class Cat:
#     def __init__(self, name, age, master):
#         self.__name = name
#         self.__age = age
#         self.__master = master
#
#         @property
#         def name(self):
#             return self.name
#
#         @name.setter
#         def name(self, name):
#             self.__name = name
#
#         @property
#         def age(self):
#             return self.age
#
#         @age.setter
#         def age(self, age):
#             self.__age = age
#
#         @property
#         def master(self):
#             return self.age
#
#         @master.setter
#         def master(self, master):
#             self.__master = master
#
#
# class Parrot:
#     def __init__(self, name, age, master):
#
#     self.__name = name
#     self.__age = age
#     self.__master = master
#
    # @property
    # def name(self):
    #     return self.name
    #
    # @name.setter
    # def name(self, name):
    #     self.__name = name
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @property
#     def master(self):
#         return self.age
#
#     @master.setter
#     def master(self, master):
#         self.__master = master

#  НАСЛЕДОВАНИЕ

# class Parent:
#     def print_world(self):
#         print('world')
#
#
# class Child(Parent):
#     def print_hello(self):
#         print('hello')
#
#
# a = Child()
#
# a.print_hello()
# a.print_world()

#  11.10
# создать родительский класс Pet, содержаший все общие методы классов Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet. Удадить в дочерних классах те методы, которые имеются у
# родительского класа. Создать объект кажого класса и вызвать его методы.




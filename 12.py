# class A:
#     def do_something(self):
#         print('AA')
#
#
# class B(A):
#     def do_something(self):
#         print('BB')
################################################################################

# 12.01

# class Pet:
#     def __init__(self, name: str, height: int, weight: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     def change_weight(self, weigth):
#         self.weight = weigth
#
#     def change_height(self, height):
#         self.height = height
#
#
# class Parrot(Pet):
#     def change_weight(self):
#         self.weight += 0.05
#
# kesha = Parrot('Kesha', 10, 5)
#
# print(kesha.name, kesha.weight, kesha.height)
################################################################################
# class A:
#     def do_something(self):
#         print('AA')
#
#
# class B(A):
#     def do_something(self):
#         super().do_something()
#         print('BB')
################################################################################
# 12.02

# Добавить метод jump, принимающий высоту прыжка. Метод выводит сообщение "Jump X meters"
# Переопределить метод jump в дочерних классах. Если передать методу jump класса dog значение больше 0.5,
# выводить сообщение "Dogs cannot jump so high", аналогично для кошек (2), для попугаев (0.05)
#
# class Pet:
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#     def jump(self, jump_hei):
#         print(f'Jump {jump_hei} meters')
#
#
# class Parrot(Pet):
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def change_weight(self, *args):
#         if args == ():
#             self.weight += 0.5
#         else:
#             self.weight += args[0]
#
#     def jump(self, jump_hei):
#         if jump_hei > 0.05:
#             print('Parrots cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#
# class Dog(Pet):
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def jump(self, jump_hei):
#         if jump_hei > 0.5:
#             print('Dogs cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#
# class Cat(Pet):
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def jump(self, jump_hei):
#         if jump_hei > 2:
#             print('Cats cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#
# #####################################
#
# kesha = Parrot('kesha', 2, 'Mom', 6, 2)
# cat = Cat('hw', 23, 'grwe', 3, 2)
# dog = Dog('fgd', 23, 'fgd', 3, 2)
#
# kesha.jump(3)
# kesha.jump(0.05)
# dog.jump(3)
# dog.jump(0.45)
# cat.jump(3)
# cat.jump(1)


# ДОБАВЛЕНИЕ АТРИБУТОВ В ДОЧЕРНИЙ КЛАСС

################################################################################
# class A:
#     def __init__(self, a):
#         self.a = a
#
#
# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b
################################################################################


# 12.03  Добавить в класс Parrot новый атрибут - species
#
# class Pet:
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#     def jump(self, jump_hei):
#         print(f'Jump {jump_hei} meters')
#
#
# class Parrot(Pet):
#     def __init__(self, name, age, master, weight, height, species):
#         super().__init__(name, age, master, weight, height)
#         self.species = species
#
#     def change_weight(self, *args):
#         if args == ():
#             self.weight += 0.5
#         else:
#             self.weight += args[0]
#
#     def jump(self, jump_hei):
#         if jump_hei > 0.05:
#             print('Parrots cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#
# class Dog(Pet):
#     def __init__(self, name, age, master, weight, height):
#         super().__init__(name, age, master, weight, height)
#
#     def jump(self, jump_hei):
#         if jump_hei > 0.5:
#             print('Dogs cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
# class Cat(Pet):
#     def __init__(self, name, age, master, weight, height, species):
#         super().__init__(name, age, master, weight, height)
#         self.species = species
#
#     def jump(self, jump_hei):
#         if jump_hei > 2:
#             print('Cats cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
# #####################################333
#
# kesha = Parrot('kesha', 2, 'Mom', 6, 2)
# cat = Cat('hw', 23, 'grwe', 3, 2)
# dog = Dog('fgd', 23, 'fgd', 3, 2)
#
# kesha.jump(3)
# kesha.jump(0.05)
# dog.jump(3)
# dog.jump(0.45)
# cat.jump(3)
# cat.jump(1)

# print(kesha.weight)
# kesha.change_weight()
# print(kesha.weight)

# 12.04

# class Pet:
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#     def jump(self, jump_hei):
#         print(f'Jump {jump_hei} meters')
#
#     def voice(self):
#         pass
#
#
# class Parrot(Pet):
#     def __init__(self, name, age, master, weight, height, species):
#         super().__init__(name, age, master, weight, height)
#         self.species = species
#
#     def change_weight(self, *args):
#         if args == ():
#             self.weight += 0.5
#         else:
#             self.weight += args[0]
#
#     def jump(self, jump_hei):
#         if jump_hei > 0.05:
#             print('Parrots cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#
# class Dog(Pet):
#     def __init__(self, name, age, master, weight, height):
#         super().__init__(name, age, master, weight, height)
#
#     def jump(self, jump_hei):
#         if jump_hei > 0.5:
#             print('Dogs cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#     def voice(self):
#         print('meow')
#
# class Cat(Pet):
#     def __init__(self, name, age, master, weight, height, species):
#         super().__init__(name, age, master, weight, height)
#         self.species = species
#
#     def jump(self, jump_hei):
#         if jump_hei > 2:
#             print('Cats cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#     def voice(self):
#         print('owa owa')
#
# #####################################333
#
# kesha = Parrot('kesha', 2, 'Mom', 6, 2, 'new')
# cat = Cat('hw', 23, 'grwe', 3, 2, 'new')
# dog = Dog('fgd', 23, 'fgd', 3, 2)
#
# def my_func(*args):
#     for i in args:
#         i.voice()
#
# print(my_func(kesha, cat, dog))
#
# print(dir(Cat))

#########################################
# class Car:
#     last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.last_model = model
#
# car1 = Car('A')
# print(Car.last_model)
# car2 = Car('B')
# print(Car.last_model)
# print(car1.last_model)
#########################################

# 12.06

# class Pet:
#     __counter = 0
#
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#         Pet.__counter += 1
#     @property
#     def counter(self):
#         return self.__counter
#     @counter.setter
#     def counter(self, counter):
#         self.__counter = counter
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#     def jump(self, jump_hei):
#         print(f'Jump {jump_hei} meters')
#
#     def voice(self):
#          pass
#
#
# class Parrot(Pet):
#     def __init__(self, name, age, master, weight, height, species):
#         super().__init__(name, age, master, weight, height)
#         self.species = species
#
#     def change_weight(self, *args):
#         if args == ():
#             self.weight += 0.5
#         else:
#             self.weight += args[0]
#
#     def jump(self, jump_hei):
#         if jump_hei > 0.05:
#             print('Parrots cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#
# class Dog(Pet):
#     def __init__(self, name, age, master, weight,  height):
#         super().__init__(name, age, master, weight, height)
#
#     def jump(self, jump_hei):
#         if jump_hei > 0.5:
#             print('Dogs cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#     def voice(self):
#         print('meow')
#
# class Cat(Pet):
#     def __init__(self, name, age, master, weight, height, species):
#         super().__init__(name, age, master, weight, height)
#         self.species = species
#
#     def jump(self, jump_hei):
#         if jump_hei > 2:
#             print('Cats cannot jump so high')
#         else:
#             super().jump(jump_hei)
#
#     def voice(self):
#         print('owa owa')
#
#
# ####################################
#
# kesha = Parrot('kesha', 2, 'Mom', 6, 2, 'new')
# cat = Cat('hw', 23, 'grwe', 3, 2, 'new')
# dog = Dog('fgd', 23, 'fgd', 3, 2)
#
# print(cat.counter)
# print(dog.counter)
# print(kesha.counter)

# МЕТОДЫ КЛАССА

# class Car:
#     __last_model = None                      # методы класса - методы которые доступны напрямую из класса
#     def __init__(self, model):               # Методы экземпляров - требуют обращения через экземпляр класса
#         self.model = model                   # Методы класса - позволяют обращаться как через экземпляр класса, так и
#         Car.__last_model = model             #  через сам класс. Могут оперировать только атрибутами класса
#     @classmethod
#     def get_last_model(cls):
#         return cls.__last_model
#
# car1 = Car('A')
# car2 = Car('BMW')
# car3 = Car('Audi')
# print(Car.get_last_model())

# 13.01 Создать метод класса get_counter. Создать три объекта. Вызвать через класс метод get_counter

class Pet:
    @classmethod
    def get_counter(cls):
        return cls.__get_counter

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1
    @property
    def counter(self):
        return self.__counter
    @counter.setter
    def counter(self, counter):
        self.__counter = counter

    def change_weight(self, weight):
        self.weight = weight

    def jump(self, jump_hei):
        print(f'Jump {jump_hei} meters')

    def voice(self):
         pass


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def change_weight(self, *args):
        if args == ():
            self.weight += 0.5
        else:
            self.weight += args[0]

    def jump(self, jump_hei):
        if jump_hei > 0.05:
            print('Parrots cannot jump so high')
        else:
            super().jump(jump_hei)


class Dog(Pet):
    def __init__(self, name, age, master, weight,  height):
        super().__init__(name, age, master, weight, height)

    def jump(self, jump_hei):
        if jump_hei > 0.5:
            print('Dogs cannot jump so high')
        else:
            super().jump(jump_hei)

    def voice(self):
        print('meow')

class Cat(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def jump(self, jump_hei):
        if jump_hei > 2:
            print('Cats cannot jump so high')
        else:
            super().jump(jump_hei)

    def voice(self):
        print('owa owa')


####################################

kesha = Parrot('kesha', 2, 'Mom', 6, 2, 'new')
cat = Cat('hw', 23, 'grwe', 3, 2, 'new')
dog = Dog('fgd', 23, 'fgd', 3, 2)

print(cat.counter)
print(dog.counter)
print(kesha.counter)

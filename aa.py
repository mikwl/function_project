class Pet:
    __counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1

    @classmethod
    def get_counter(cls):
        return cls.__counter


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species


class Dog(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)


class Cat(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species


kesha = Parrot('kesha', 2, 'Mom', 6, 2, 'new')
print(Parrot.get_counter())
cat = Cat('hw', 23, 'grwe', 3, 2, 'new')
print(Cat.get_counter())
dog = Dog('fgd', 23, 'fgd', 3, 2)
print(Dog.get_counter())

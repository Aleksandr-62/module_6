class Animal:
    """
    Класс животные (родительский)
    """
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False


class Mammal(Animal):
    """
    Подкласс животные (дочерний)
    """
    pass


class Predator(Animal):
    """
    Подкласс животные (дочерний)
    """
    pass
    pass


class Plant:
    """
    Класс еда (родительский)
    """
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    """
    Подксласс еда (дочерний)
    """
    pass


class Fruit(Plant):
    """
    Подксласс еда (дочерний)
    """
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
class Fruit():
    """ This is a class that will cut and taste ripe fruits """
    def __init__(self, name, color, ripe):
        self.name = name
        self.color = color
        self.ripe = ripe
        self.cut = False
        self.taste = 'unknown'

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.name, self.color, self.ripe, self.cut, self.taste)
    
    def cut_fruit(self):
        if self.ripe:
            self.cut = True

    def taste_fruit(self):
        if self.cut:
            self.taste = 'great'

fruit1 = Fruit('mango', 'yellow', True)
print(fruit1)
fruit1.cut_fruit()
fruit1.taste_fruit()
print(fruit1)

fruit1 = Fruit('orange', 'orange', False)
print(fruit1)
fruit1.cut_fruit()
fruit1.taste_fruit()
print(fruit1)
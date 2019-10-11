# class starts with capital letter
# "self" references the current object
# to make a child class, simply add (NameOfParentClass) after the name. It will inherrit all the methods and shit


class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # methods
    def move(self):
        print("move")

    def draw(self):
        print("draw")

    # properties
    z = 3


# creating an istance
point1 = Point(11, 20)

# assigning atributes

point1.y = 21


point1.draw()
print(point1.x)

point2 = Point(1, 2)
print(point2.z)

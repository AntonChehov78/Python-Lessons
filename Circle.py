

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a*self.b

class Squaree:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a**2

# Выполните задание, взяв за основу полученный код из задания 21.8.1.
# Добавьте еще один класс — круг (class Circle), который принимает в качестве аргументов свой радиус.
# Вычислите площадь круга
import math
class circle:
    def __init__(self, r):
        self.r = r
    def get_area_circle(self):
        return math.pi *(self.r**2)
class Triangle:
    def __init__(self, x, y, side_a, side_b, side_c, p):
        self.x = x
        self.y = y
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.p = (self.side_a+self.side_b+self.side_c)/2

    def __str__(self):
        return f'Triangle : {self.x}, {self.y}, {self.side_a}, {self.side_b}, {self.side_c}, {self.p} '
    def get_area(self):
        return (self.p*(self.p-self.side_a)*(self.p-self.side_b)*(self.p-self.side_c)) ** 0.5

trian = Triangle (5, 3, 50, 50, 50,())
print(trian)
print(int(trian.get_area()))
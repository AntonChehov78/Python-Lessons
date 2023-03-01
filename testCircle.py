

from Circle import Rectangle, Squaree, circle
r1 = Rectangle(10,5)
r2 = Rectangle(7,15)
# print(r1.get_area())
# print(r2.get_area())
#
r_square1=Squaree(5)
r_square2=Squaree(8)
# print(r_square1.get_area_square(),
#       r_square2.get_area_square())

r_circle = circle(10)
# print(r_circle.get_area_circle())

figures=[r1, r2, r_square2, r_square1, r_circle]
for figure in figures:
      if isinstance(figure, Rectangle):
            print(figure.get_area())
      elif isinstance(figure, Squaree):
            print(figure.get_area_square())
      else:
            print(figure.get_area_circle())


# from Circle import circle
# r_circle = circle(10)
# print(r_circle.get_area_circle())

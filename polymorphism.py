#polymorphism is many forms a method can take
class Rectangle:
    def draw(self):
        print("Drawing a Rectangle")

class Rhombus():
    def draw(self):
        print("Drawing a Rhombus")

class Parallelogram():
    def draw(self):
        print("Drawing a Parallelogram")

r = Rectangle()
r.draw()

rh = Rhombus()
rh.draw()

p = Parallelogram()
p.draw()

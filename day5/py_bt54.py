class Shape(object):
    def __init__(self):
       pass

    def area(self):
       return 0
class Square(Shape):
    def __init__(self, l):
       Shape.__init__(self)
       self.length = l

    def area(self):
       return self.length*self.length

aSquare= Square(3)
print (aSquare.area())

# hi đè một method trong super class, chúng ta có thể định nghĩa một method có cùng tên trong super class.
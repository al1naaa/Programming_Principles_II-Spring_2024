import math
class Point:
    def __init__(self, x1, y1):
        self.x1=x1
        self.y1=y1
    def show(self):
        print("Coordinates: ", self.x1, self.y1) 
    def move(self, x2, y2):
        self.x2=x2
        self.y2=y2
        print("Next coordinates:",self.x2, self.y2)
    def dist(self):
        print("Distance between two points:",math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2))

x=Point(int(input()), int(input()))
x.show()
x.move(int(input()), int(input()))
x.dist()
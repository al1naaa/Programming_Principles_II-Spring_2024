class MyClass:   
    def getString(self):
        self.a=str(input())
    
    def printString(self):
        print(self.a.upper())

p1=MyClass()
p1.getString()
p1.printString()
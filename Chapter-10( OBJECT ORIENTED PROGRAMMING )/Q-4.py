# 4. Add a static method in problem 2, to greet the user with hello. 

class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")    
    def Cube(self):
        print(f"The cube is {self.n*self.n*self.n}")    
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")    

    @staticmethod
    def hello():
        print("Hello there!")
num = int(input("Enter a number"))        
a = Calculator(num)
a.square()     
a.Cube()
a.squareroot()   
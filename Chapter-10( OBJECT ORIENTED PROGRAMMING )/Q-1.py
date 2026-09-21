# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry",12000,841203)   
print(p.name,p.salary,p.pin,p.company)     
p = Programmer("prakash",15000,741203)   
print(p.name,p.salary,p.pin,p.company)     
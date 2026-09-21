# 1. Write a program using functions to find greatest of three numbers. 

def gratest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
a=9 
b=5
c=3
print(gratest(a,b,c))
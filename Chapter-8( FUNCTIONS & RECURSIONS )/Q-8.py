# 8. Write a python function to print multiplication table of a given number. 

n = int(input("Enter a value"))
def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
multiply(n)
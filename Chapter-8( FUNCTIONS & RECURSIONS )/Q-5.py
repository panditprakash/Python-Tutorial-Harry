# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 

i = int(input("Enter a value"))
def pattern(i):
    if(i==0):
        return
    print("*" * i)
    pattern(i-1)
pattern(i)


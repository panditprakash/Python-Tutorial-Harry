# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S. l = ["Harry", "Soham", "Sachin", "Rahul"] 


l =["harry","Soham","sachin","rahul"]

for name in l:
    if(name.startswith("h")):
        print(f"hello {name}")
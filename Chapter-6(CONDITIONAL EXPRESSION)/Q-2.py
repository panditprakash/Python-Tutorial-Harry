# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

maths = int(input("Enter a maths score"))
physics = int(input("Enter a physics score"))
chemistry = int(input("Enter a chemistry score"))

total_percentage =((100)*(maths+physics+chemistry))/300
if(total_percentage>=40 and maths>=33 and chemistry>=33 and physics>=33):
    print("you are pass",total_percentage)
else:
    print("you are failed, try again next year",total_percentage)

print("students marks is",total_percentage);
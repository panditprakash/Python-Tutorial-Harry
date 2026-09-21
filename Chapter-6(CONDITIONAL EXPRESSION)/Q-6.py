# 6. Write a program to calculate the grade of a student from his marks from the following scheme: 90 – 100 => Ex 80 – 90 => A 70 – 80 => B 60 – 70  =>C 50 – 60 => D <50        => F

# marks = int(input("Enter your marks"))

# if(marks<=100 and marks>=90):
#     print("Ex")
# elif(marks<90 and marks>=80):
#     print("A")
# elif(marks<80 and marks>=70):
#     print("B")
# elif(marks<70 and marks>=60):
#     print("C")
# elif(marks<60 and marks>=50):
#     print("D")
# elif(marks<50):
#     print("F")

#     print("your grade is :", print)

# # 6. Write a program to calculate the grade of a student from his marks from the following scheme: 90 – 100 => Ex 80 – 90 => A 70 – 80 => B 60 – 70  =>C 50 – 60 => D <50        => F

Marks = int(input("Enter a marks:-"))
if(Marks <= 100 and Marks >= 90):
    print("Your Performance is Ex")
elif(Marks <= 90 and Marks >= 80):
    print("Your Performance is A") 
elif(Marks <=  80 and  Marks >= 70 ):
     print("Your Performance is B")
elif(Marks <= 70 and Marks >= 60):
    print("Your Performance is C")
elif(Marks <= 60 and Marks >=50):
    print("Your Performance is D")
elif(Marks >= 50):
    print("Your Performance is Fail")             

print("Your marks is =",Marks)
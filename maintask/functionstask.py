# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,
# then a functions that finds the grade according to the table below. 
# Use the value from total to get the average and average to find the grade.
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


# maths = float(input("Enter maths score: "))
# eng = float(input("Enter english score: "))
# swa = float(input("Enter swahili score: "))
# sci = float(input("Enter science score: "))
# sos = float(input("Enter sos score: "))


# def total_marks(a,b,c,d,e):
#     total_marks = (a + b + c + d + e)
#     print(f'Total marks is {total_marks}')

# total_marks(maths,eng,swa,sci,sos)


# def average_marks(a,b,c,d,e):
#     average_marks = (a + b + c + d + e)/5
#     print(f'Average marks is {average_marks}')

# average_marks(maths,eng,swa,sci,sos)


# def grade(a,b,c,d,e):
#     average_marks = (a+b+c+d+e)/5
#     result = average_marks
#     if result > 79:
#         grade = "A"
#     elif result >=60 and result <= 79:
#         grade = "B"
#     elif result >= 49 and result <= 59:
#         grade = "C"
#     elif result >= 40 and result < 49:
#         grade = "D"
#     else:
#         grade = "E"

#     # print(result)
#     print(f'Grade is {grade}')
# grade(maths,eng,swa,sci,sos)


# Write a program which gets a phone number from a form input or terminal.
# Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... 
# Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

def phone_number(num):
    if num[0:4] == "+254"  and len(num) == 13:
        result = num
    elif num[0:3] == "254" and len(num) == 12:
        result = "+"+num
        
    elif num[0:2]=="07" or num[0:2]== "01" and len(num) == 10:
        result = "+254" + num[1:]
       
    elif num[0] == "7" or num[0] == "1" and len(num) == 9:
        result = "+254" + num
  
    else:
        result = "Invalid number"
  
    return result
num = input("Enter phone number: ")
phone = phone_number(num)
print(phone)

# implement a program that takes 3 form inputs or from the terminal, and stores them in three variables.
# aReturn the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

# def numbers(num1,num2,num3):
#     if num1 > num2 and num1 > num3:
#         result = "num1 is the largest"
#     elif num2 > num1 and num2 > num3:
#         result = "num2 is the largest"
#     else:
#         result = "num3 is the largest"
#     return result
    
# num1  = float(input("Enter num1: "))
# num2  = float(input("Enter num2: "))
# num3  = float(input("Enter num3: "))
# num = numbers(num1,num2,num2)
# print(num)
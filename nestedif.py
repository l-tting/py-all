# # score = int(input("Enter your score: "))
# # if score >=0 and score <=100:
# #     if (score >=90):
# #         grade  = "A"
# #     elif (score >= 80) and (score < 90):
# #         grade = "B"
# #     elif (score >= 70) and (score < 80):
# #         grade = "C"
# #     elif (score >= 60) and (score < 70):
# #         grade = "D"
# #     elif (score >= 50) and (score < 60):
# #         grade = "E"
# #     else:
# #         grade = "Fail"
# # else:
# #     grade ="Invalid score"
# # print(grade)

#              #no 2
input1 = float(input("Enter first no: "))
input2 = float(input("Enter second no: "))
sum = input1 + input2
if (input1 >= 0) and (input2 >= 0):
    if sum%2 == 0:
        result ="Even sum"
    else:
        result= "Odd sum"
else:
    result="Negative number"
print(result)

#              #no1
# #write  program  that takes student scores input checks if the scores are btwn 0 and 100 and prints their grade
# #A 90 and above B 80 -89 C 70 -79  D 60 -69 F Below 60
# score = float(input("Enter your score: "))
# if score >= 0 and score <= 100:
#     if score >= 90:
#         result = "A"
#     elif score >= 80 and score < 90:
#         result = "B"
#     elif score >= 70 and score < 80:
#         result = "C"
#     elif score >= 60 and score < 70:
#         result = "D"
#     else:
#         result = "F"
# else:
#     result = "Invalid score"
# print(result)


#             #no3
# #Create program that takes users input for a time in 24hr format and converts  it to 12 hour format.
# #Consider  handling cases for noon and midnight appropriately.

time = (input("Enter time in h: min: "))
time2 = time.split(":")
hh= int(time2[0])
mm= int(time2[1])

if (hh>= 0 and hh <= 23) and mm >= 0 and mm <= 59:
    if hh > 12 :
        h = hh- 12
        h = str(h) +  ":"  +  str(mm)+ "PM"
        print(h)


    elif hh < 12 and hh > 0:
        h = str(hh) + ":" + str(mm) + "AM"
        print(h)
    elif hh == 0 and mm > 0:
        h = hh + 12
        h = str(h)+ ":" + str(mm)  + "AM"
        print(h)
    elif hh == 0 and mm == 0:
        h = hh +12
        h = "Midnight"
        h = "12:00am"
        print(h)
    elif hh == 12 and mm == 0:
        print("Noon")
        print("12:00pm")
        
else:
    print("Invalid time")



 


     
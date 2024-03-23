# Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”.
# demerit = 0
# limit = 12
# out_of_limit = False
# speed = int(input("Enter speed: "))
# while speed > 70 and not(out_of_limit):
#     if demerit < limit:
#         points= (speed - 70)/5
#         demerit+=points
#     el:

speed = int(input("Enter speed: "))
speed_limit =70 
points = 0

if speed < speed_limit :
    print("Ok")
else:
    if speed> 70 and speed < 75:
        points = 1
    else:
       points = (speed - speed_limit)//5
       print(f"Demerit points: {points}")
    if points > 12:
        print("License suspended")
    else:
        print(f"You have {points} demerit points")
    







            
        

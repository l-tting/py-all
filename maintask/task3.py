# Write a program which gets a phone number from a form input or terminal. 
# Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01...
#  Convert the number to start with +254… 


number  = input("Enter phone number: ")

if number[0:4] == "+254" and len(number) == 13:
    print(number)
elif number[0:2]== "07" or number[0:2] == "01" and len(number)== 10:
      print("+254" + number[1:])
elif number[0]== ("7") and number[0]== "1" and len(number)==9:
        print("+254" + number[0:1])
elif number[0:3] == "254" and len(number)==12:
      print("+" + number)

else:
      print("Invalid number")
      


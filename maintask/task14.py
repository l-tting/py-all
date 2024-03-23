# Write a program that takes input of 2 values and adds them.
# The program should only accept numbers and floats only 
# or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .

# while True:
#     try:
#        num1 = int(input("Enter first number: "))
#        num2 = int(input("Enter second number: "))
#        result = num1 + num2
#        print(result)
#        break
#     except ValueError:
#        print("Invalid character entered")
       
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == "int" or num1 == "float":
    print("Invalid character entered")
else:
     result = num1 + num2   
     print(result)

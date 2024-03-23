#Write a program which accepts email as form input or from terminal.
#Validate the email by checking if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.
email = input("Enter your email: ")
for i in range(0,(len(email)+1)):
    if "@"  in email and "." in email:
        if email[i]== "@":
            at = i
        elif email[i]== ".":
            dot = i
        if at <dot and at>1 and dot <len(email)-1:
            print("email valid")
    else:
        print("Invalid email")


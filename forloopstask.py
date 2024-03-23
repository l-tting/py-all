# Write a program that displays a numbers 1 to 50 inside a list.
display  = []
for i in range(1,51):
    display.append(i)
# print(display)


# # From 1 above display the ones divisible by 7 or 5 inside a list.
display2 =[]
for i in display:
    if (i%7==0) or (i%5==0):
        display2.append(i)
# print(display2)


# Find sum and average of values in the range between 10 to 40.
sum = 0
display3  = []
for i in range(10,41):
    display3.append(i)
    sum = sum +  i
    av = sum/(len(display3))
# print(display3)   
# print(sum)
# print(av)


# Put in a list the first 10 odd numbers between 10 to 50. 
display4 = []
for i in range(10,51):
    if i%2 != 0:
        display4.append(i)
    print(display4[0:10])


# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# num = int(input("Enter number: "))
for i in range(0,11):
    product = num * i
    # print(num,"x",i ,'=', product)


# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
display5 = []
for i in range(1,51):
    if i%2 == 0:
        display5.append(i)
# print(display5)
# print(len(display5))

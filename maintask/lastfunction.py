# Celcius to farenheit
temperature= float(input("Enter temp in celcius: "))
def temp(a,b=9/5,c=32):
    far = (a * b) + c
    return far
farenheit = temp(temperature)
print(farenheit)


# Write a function called reverse string that takes a string as a parameter and returns the reverse.
string = input("Enter string: ")
def reverse_string(string):
    string = string[::-1]
    return string
reverse = reverse_string(string)
print(reverse)


# Write a function called square that takes a number as a parameter and returns its square.
num = float(input("Enter number: "))
def square(a,b=2):
    square = a**b
    return square
sq = square(num)
print(sq)
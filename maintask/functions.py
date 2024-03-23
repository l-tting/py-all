def hello(a):
    print(f"Hello {a}")

# name = input("Enter your name: ")
# hello(name)

def triangle(b,h):
    area = (b*h)/2
    print(area)

# triangle(34,34)

#function to calculate area of a rectangle after taking length and width from user
def rectangle(l,w):
    area = l*w
    print(area)
length = float(input("Enter length: "))
width = float(input("Enter width: "))
rectangle(length,width)


def odd_even(a):
    if a%2 == 0:
        print("Even")
    else:
        print("Odd")
num = float(input("Enter no.: "))
odd_even(num)
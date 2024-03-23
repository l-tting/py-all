#convert a float to an integer with an inbuilt function
#temp  = 56.8926
temp = 56.8926
temp = int(temp)
print(temp)

#convert float to give temp = 56.8926 to 56.89
temp = 56.8926
temp = round(temp,2)
print(temp)

#convert float to give temp = 56.8926 to 56.893
temp = 56.8926
temp = round(temp,3)
print(temp)

#convert float top give temp = 56.8926 to 8.926
temp = 56.8926
temp = str(temp)
temp = temp[3:7]
print(temp)
temp =(temp[0] + "." + temp[1:4])
print(temp)


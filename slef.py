#having the string r ='["E","W","C"]' manipulate it to display EWC
r = '["E","W","C"]'
r = ''.join(filter(str.isalpha,r))
print(filter(str.isalpha,r))
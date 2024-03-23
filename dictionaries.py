days = {
    "Mon" : "Monday",
    "Tue" : "Tuesday",
    "Wed" : "Wednesday",
    "Thur": "Thursday",
    "Fri" : "Friday",
    "Sat" : "Saturday",
    "Sun" : "Sunday",
}
# print(days["Sun"])

person = {"name":"Brian", 
          "age": 24,  
          "location": "Nairobi",
          "email": "brianletting01@gmail.com",
          "address": [101,"Nairobi"]
        
}
print(person['location'])
print(person['age'])
print(person['address'])

person["name"] = "Kevin"
person["location"]  = "Nakuru"
person["address"] = [101,"Nairobi"]

person["occupation"] = "d.e"
# checking if a key is in a dict
print("name" in  person)
print("occupation" in person)

student={"name":"Darshan","age":23,"courses":["Mechanical","frontend development","React"]}
print(student["courses"][0])#  this is one way of accessing data from dictionary 
# another way of accessing data from dictionary 


print(student.get("name")) # by using get method we can access the data from dictionary
print(student.get("phone","Not Found"))


student["phone"]=9886849137 # one way of adding data to the dictionary 
student.update({"perfume":"Gucci"}) # using update method we can add the data in end of the dictionary
print(student)


# to remove the item from dictionary 
# del student["age"]
# print(student)  one way of removing the data from dictionary is by using del function 
age=student.pop("age")
print(age)  # another way of popping the item from dictionary 


print(len(student)) #we can checkout the length of the dictionary with the len method 
print(student.keys()) # we can print all the keys through this method
print(student.values()) # we can print all the values present in the dictionary by using this method

print(student.items()) # it will return us a key and a value pair of the dictionary 


for items, values in student.items():
    print(items, values)



message="Hello World"
lowerMessage=message.lower()  #lower
print(lowerMessage)

print(message.upper()) #upper

print(message.count("l")) #count

print(message.find("l")) #find

# new_message=message.replace("World","python") # replace # tis replace method will return a new string so we have to store it in a new variable 

# print(new_message)


message=message.replace("World","Python")
print(message)


greeting="Hello"
name="Darshan"
message=greeting+" "+name
print(message)

message="{}, {} .Welcome".format(greeting,name)  # it is used to concat other strings with the current one 
print(message)



message=f"{greeting.upper()} {name.capitalize()} . welcome"
print(message)


print(dir(str))
courses=["math","science","social","compsci"]
print(courses)
print(len(courses))
print(courses[2])
print(courses[0:2])

courses.append("art")  # append it will add the value to the end of the nlist 
print(courses)

courses.insert(0,"commerece")  #insert it ads a value to specific position
print(courses)

courses2=["lab","Mechanical"]
courses.extend(courses2) # it wil add the other elements in the end of the list 
print(courses)

courses.remove("lab")  #it removes the item in the list whioch we specify 
print(courses)

courses.pop()  # it removes the last ite of the list 
print(courses)

courses.reverse() # it reverse the whole list 
print(courses)

courses.sort() # it sorts the list in assending order 
print(courses)

nums=[1,12,24,5,1,7,78]
nums.sort()
print(nums)


nums.sort(reverse=True) # this sorts the whole list in the dessending order 
print(nums)

# altewrnartive way of getting the sorted list without altering the original list .............................
Sorted_List=sorted(courses)
print(Sorted_List)
Sorted_Nums=sorted(nums)
print(Sorted_Nums)



print(min(nums)) #  gets the minimum value in the list 
print(max(nums)) # gets the max value in the list 
print(sum(nums))# adds everything in the list 

print(courses.index("social")) # index it fetch us out the index of the particular item in the list 

print("jaamon" in courses)  #in property lets us know whetjer the value is present or not 


# for itm in courses:
#     print(itm)


for index, item in enumerate(courses):  # enmuerate gives us the index of the index of the value 
    print(index,item)

course_str="".join(courses)


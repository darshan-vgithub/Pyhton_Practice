nums=[1,2,3,4,5,6]

for num in nums:
    for letter in "abc":
        print(num,letter)


x=0
while True:
    if x==1000:
        print("found {}".format(x))
        break
    print(x)
    x+=1
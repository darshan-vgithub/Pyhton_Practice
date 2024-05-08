def hello_func():
    return "Hello function"

print(hello_func().upper())



def Greeting(greeting=str,name=str):
    return "{}, {} how is it learning with python".format(greeting,name)

print(Greeting("Welcome","darshan").upper())


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
courses=["Math","Art"]
info={"name":"Darshan","age":23}
student_info(*courses,**info)

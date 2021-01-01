a = 2
b = 3
c = sum((a, b))  # Inbuilt function sum,also it should be list or tuple (i.e should iterable)
print(c)


# two types : user defined and build in function

# user defined
def myFunct():
    print("In function")


# Function with no input/output
print(myFunct())  # prints none(return type)
myFunct()  # calls the function


# function which takes input as well as output
def myFunct(a, b):
    """This is a function which will calculate average of 2 functions"""
    print(f"In function which takes input, {a+b}")


myFunct(4, 5)
"""This is how Docstring is written"""
print(myFunct.__doc__)
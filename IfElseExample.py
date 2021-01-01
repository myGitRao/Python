# Driving status on basis of age

print("Please enter your age: ")
age = int(input())

if (age > 5) and (age <100):
    print("Valid age entered")
    if age > 18:
        print("You can drive")
    elif age < 18:
        print("You cannot drive")
    else:
        print("You are 18,You need to give a driving test")
else:
    print("Invalid age, Enter a valid age")
# # calculate the values correctly except for the below calculations:
# # 45*3= 555
# # 56+9 =77
# # 56/6 =4
while True:
    decision = input("You wanna do operations on numbers:Press : Yes or No ")
    if decision.lower() == "yes":
        print("Inside the loop")
        inp = int(input("""Enter the operation you wanna do: 
                 1. Add
                 2.Subtract
                 3.Multiply
                 4.Divide
         """))
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        if inp == 1:
            if (a == 56) and (b == 9):
                print(f"{a} + {b} = 77")
            else:
                ans = a + b;
                print(f"{a} + {b} = {ans}")

        if inp == 2:
            ans = a - b;
            print(f"{a} - {b} = {ans}")

        if inp == 3:
            if (a == 45) and (b == 3):
                print(f"{a} + {b} = 555")
            else:
                ans = a * b
                print(f"{a} * {b} = {ans}")

        if inp == 4:
            if (a == 56) and (b == 6):
                print(f"{a} / {b} = 4")
            else:
                ans = a / b
                print(f"{a} / {b} = {ans}")
    else:
        break






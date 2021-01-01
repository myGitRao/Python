# print("Enter the number")
# num = int(input())
#
# if num > 100:
#     print("Congratulations you have entered number greater than 100")

while True:
    num = int(input("Enter the number: "))
    if num < 100:
        continue
    else:
        print("Congratulations you have entered number greater than 100")
        break


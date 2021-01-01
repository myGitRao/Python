list = ["Pooja", "int", 2, "Rao", 6, "Gargi", "Nayan", 9, 12, 43, 45.01]
for item in list:
    if type(item) == int:
        if item > 6:
            print(f"The number {item } is greater than 6")
#     elif(item == 6):
#         print(f"The number {item}","is equal to 6")
#     else:
#         print(f"The number {item}","is less than 6")
# else:
#     print(f"{item} is not an integer")


list = ["Pooja", "int", 2, "Rao", 6, "Gargi", "Nayan", 9, 12, 43, 45.01]
for items in list:
    #    if str(items).isnumeric() > 6:
    if str(items).isnumeric() and items > 6:
        print(f"The number {items} is greater ")

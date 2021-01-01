magicNum = 18
print("You have total 9 attempts to guess the number")
while True:
    print(f"""
Guess the number :""")
    guess = int(input())
    if guess != magicNum and count < 10:
        print("Hey that's a wrong guess,try again!")
        continue
    elif guess == magicNum:
        print(f"Hey! You guessed right in {count} attempts")
        break





import random


computer_number = random.randint(10, 40)
print("a random number was selected")
for i in range(10):
    user_number = int(input("enter your guess:  "))

    if computer_number == user_number:
        print("""\tyour guess is correct
        you win🥳""")
        print("you try ", i+1, "time")
        break

    elif computer_number > user_number:
        print("go up")

    elif computer_number < user_number:
        print("go down")


print("well done")

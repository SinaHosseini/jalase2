import random

while True:
    x = random.randint(1, 3)
    print("\n choice: \n 1.rock🪨 \n 2.paper📃 \n 3.scissors✂️")
    y = input("\n enter your choice or exit ")

    if "1" <= y <= "3":
        print("ready \n1 \n2 \n3 \nGo!")
        if x == 1:
            c_choice = "rock🪨"

        elif x == 2:
            c_choice = "paper📃"

        elif x == 3:
            c_choice = "scissors✂️"

        if y == "1":
            u_choice = "rock🪨"

        elif y == "2":
            u_choice = "paper📃"

        elif y == "3":
            u_choice = "scissors✂️"

        print("💻", c_choice)
        print("👤", u_choice)

        if x == 1 and y == "1":
            print("equivalent")

        elif x == 1 and y == "2":
            print("you win 😒")

        elif x == 1 and y == "3":
            print(" i win 🤪")

        elif x == 2 and y == "1":
            print(" i win 🤪")

        elif x == 2 and y == "2":
            print("equivalent")

        elif x == 2 and y == "3":
            print("you win 😒")

        elif x == 3 and y == "1":
            print("you win 😒")

        elif x == 3 and y == "2":
            print(" i win 🤪")

        elif x == 3 and y == "3":
            print("equivalent")

    elif y == "exit":
        break
    else:
        print("incorrect, try again")

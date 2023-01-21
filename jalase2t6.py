import random
while True:
    game = input("\nenter number \n1.start \nor \n2.exit: ")
    if game == "1":
        dice = random.randint(1, 6)
        print("🎲= ", dice)

        while dice == 6:
            dice = random.randint(1, 6)
            print("🎲= ", dice)

    elif game == "2":
        break

    else:
        print("try again")

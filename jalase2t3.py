i = 0
ave = 0

while True:
    score = input("enter your score or exit: ")
    if score == "exit":
        break

    else:
        ave = ave + float(score)
        i = i+1

ave = ave/i
print("avrage is: ", ave)

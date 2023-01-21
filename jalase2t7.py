while True:
    n = int(input("please enter number of Fibonachi series: "))

    fibonachi = [1]

    if n == 1:
        print(fibonachi)

    elif n == 2:
        fibonachi.append(1)
        print(fibonachi)

    elif n > 2:
        fibonachi.append(1)
        for i in range(2, n):
            fibonachii = fibonachi[i-1]+fibonachi[i-2]
            fibonachi.append(fibonachii)

        print(fibonachi)

    elif n <= 0:
        print("incorrect, please try again")

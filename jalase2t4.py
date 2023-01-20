hour = int(input("enter a hour: "))
sec = hour*3600
min = int(input("emter minute: "))
if 0 <= min < 60:
    sec = (min*60)+sec
else:
    print("wrong minute.")
print(sec)

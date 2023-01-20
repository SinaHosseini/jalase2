hour = 0
min = 0
sec = int(input("enter second: "))
if sec >= 3600:
    hour = sec/3600
    sec = sec % 3600
    if sec > 60:
        min = sec/60
        sec = sec % 60

elif sec < 3600:
    min = sec/60
    sec = sec % 60


print("time is: ", int(hour), ":", int(min), ":", sec)

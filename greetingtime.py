import datetime
a=datetime.datetime.now().hour
print(a)
if (5<=a<12) :
    print("Good Morning")
elif (12<=a<17) :
    print("Good afternoon ")
elif (17<=a<20) :
    print("Good evening")
else :
    print("Good night")


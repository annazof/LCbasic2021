time=input("What time is it?")
t=int(time)

hours=input("how many hours till alarm?")
h=int(hours)

alarm=(t+h)%24
print("Time of the alarm",alarm)


respone=input("Please enter the number of your day from 0 to 7")
n=int(respone)

if n == 0:
    print("Sunday")
elif n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
else:
    print("Invalid")

#Alternative solution
week_days = ["Sunday", "Monday", "Tuesday", "Wednesdau", "Thursday", "Friday", "Saturday"]

today = int(input("What day is today? (0-6) "))

print("Today is", week_days[today])
today=int(input("What is the day today? Choose from 1 to 7"))
no_of_days=int(input("How many days are you staying"))

total= today+ no_of_days
finans = total % 7

if finans==1:
    print("You will return on Moday")
elif finans==2:
    print("You will return on Tuesday")
elif finans==3:
    print("You will return on Wednesday")
elif finans ==4:
    print("You will return on Thursday")
elif finans == 5:
    print("You will return on Friday")
elif finans == 6:
    print("You will return on Saturday")
elif finans ==7:
    print("You will return on Sunday")
else:
    print("Invalid request")

#Alternative solution by Vincent
week_days = ["Sunday", "Monday", "Tuesday", "Wednesdau", "Thursday", "Friday", "Saturday"]

today = 3       # int(input("What is the start day? (0-6) "))
sleeps = 137    # int(input("How many sleeps?")

print("You will return on", week_days[(today + sleeps) % len(week_days)])
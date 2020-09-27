numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for number in numbers:
    if number < 40:
        print("Grade F3")
    elif 40 <= number<45:
        print("Grade F2")
    elif 45 <= number < 50:
        print("Grade F1 Supp")
    elif 50 <= number<60:
        print("Grade Third")
    elif 60 <= number<70:
        print("Grade Second")
    elif 70 <= number<75:
        print("Grade Upper Second")
    elif 75 <= number:
        print("Grade First")
    else:
        print("Invalid input")


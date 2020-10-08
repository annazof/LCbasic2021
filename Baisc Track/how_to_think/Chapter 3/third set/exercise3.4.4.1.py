#Write a program to count how many odd numbers are in a list.
numb = [2,3,5,6,23,46,98,79]

count = 0
for i in numb:
    if i % 2 == 1:
        count += 1

print(count)
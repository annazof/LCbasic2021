#Write a program that computes the sum of the squares of the numbers in the list numbers. For example a call
#with, numbers = [2, 3, 4] should print 4+9+16 which is 29.

numbers=[2,1,2]

count=0
for i in numbers:
    count+=i**2

print(numbers, "which is", count)
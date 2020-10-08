#Write a program that prints out the first n triangular numbers.

n=int(input("Pick a number"))

count=0
for i in range(1,n+1):
    print(i, "\t", i+count )
    count+=i

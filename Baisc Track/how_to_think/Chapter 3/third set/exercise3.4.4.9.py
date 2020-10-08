#Write a program which prints True when n is a prime number and False otherwise.

n=int(input("Choose a number"))

for i in range (2,n):
    if n%i==0:
        print(False)
        break
    else:
        print(True)
        break


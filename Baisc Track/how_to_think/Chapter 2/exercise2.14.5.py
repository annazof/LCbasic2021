response = input("What is your initial investment? ")
p = float(response)

answer=input("How many years will you keep your investment?")
t=int(answer)

#interest rate
i=0.01

#number of times the interest is compunded per year
n=4

a=p*(1+i)**(n*t)

print("The final amount is ", a)
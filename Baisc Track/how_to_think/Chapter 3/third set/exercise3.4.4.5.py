#5. Sum all the elements in a list up to but not including the first even number. (What if there is no even number?)

numbers=[3,5,1,1,4,5,6]

count=0

for i in numbers:
    if i%2==1:
        count +=i
    else:
        break

print(count)
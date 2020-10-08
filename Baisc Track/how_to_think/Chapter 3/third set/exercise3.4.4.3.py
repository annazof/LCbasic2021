#3. Sum up all the negative numbers in a list.

numb = [2,3,-5,6,23,-46,98,-79]

count = 0
for i in numb:
    if i < 0:
        count += i

print(count)
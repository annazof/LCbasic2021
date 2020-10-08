#4. Count how many words in a list have length 5
words=["add","dog","might", "power", "grade", "butterfly"]

count=0
for w in words:
    if len(w)==5:
        count +=1

print(count)
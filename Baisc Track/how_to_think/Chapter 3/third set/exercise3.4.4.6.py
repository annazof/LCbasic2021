#Count how many words occur in a list up to and including the first occurrence of the word “sam”. (What if
#“sam” does not occur?)

words=["sally","5","fun","day","sam","full","fool"]

count=0

for w in words:
    if w=="sam":
        count +=1
        break
    else:
        count +=1

print(count)

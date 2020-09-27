numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#a)
for i in numbers:
    print(i)

#b)
for i in numbers:
    print(i, "\t", i**2 )
#c)
total=0
for i in numbers:
    total += i
print(total)

#d)
final=1
for i in numbers:
    final *=i
print(final)
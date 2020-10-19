#5. Write a program that takes the dictionary used above, and returns some of the words using 1337sp34k

with open("C:\\Users\\Anna\\Desktop\\Learning Community\\poem.txt", "r") as infile, open("C:\\Users\\Anna\\Desktop\\Learning Community\\1337sp34k.txt","w") as outfile:
    for line in infile:
        line=line.replace("the", "1337sp34k" )
        outfile.write(line)
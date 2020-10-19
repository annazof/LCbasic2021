
with open("C:\\Users\\Anna\\Desktop\\Learning Community\\poem.txt", "r") as infile, open("C:\\Users\\Anna\\Desktop\\Learning Community\\copypoem.txt","w") as outfile:
    count=1
    for line in infile:
        newline="{0:>4} {1}".format(count,line)
        outfile.write(newline)
        count+=1






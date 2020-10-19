
with open("C:\\Users\\Anna\\Desktop\\Learning Community\\copypoem.txt", "r") as infile, open("C:\\Users\\Anna\\Desktop\\Learning Community\\blank.txt","w") as outfile:
    for line in infile:
        outfile.write(line[5:])






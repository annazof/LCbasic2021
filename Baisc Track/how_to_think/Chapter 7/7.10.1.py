wordsfile = open("C:\\Users\\Anna\\Desktop\\Learning Community\\lcpython.txt", "r")
newfile= open("C:\\Users\\Anna\\Desktop\\Learning Community\\output.txt", "w")

with open("C:\\Users\\Anna\\Desktop\\Learning Community\\lcpython.txt", "r") as infile, open("C:\\Users\\Anna\\Desktop\\Learning Community\\output.txt","w") as outfile:
    content = infile.read()
    words = content.split()
    words.reverse()
    print(words)
    for w in words:
        outfile.write(w+ " ")
    print(outfile)



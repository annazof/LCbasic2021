
def replace(s, old, new):
    s=list(s)
    for i in range(len(s)):
        if s[i]==old:
            s[i]=new
    print("".join(s))

replace("Mississippi", "i", "I")
#== "MIssIssIppI"
song = "I love spom! Spom is my favorite food. Spom, spom, yum!"
replace(song, "om", "am")
#== "I love spam! Spam is my favorite food. Spam, spam, yum!"
replace(song, "o", "a")
#==  "I lave spam! Spam is my favarite faad. Spam, spam, yum!"

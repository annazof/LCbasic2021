
count=0
def mirror(word):
    """
    Reversing the string
    :param input: word
    :return: reversed word
    """
    w=""
    count = -1
    for i in word:
        w+=word[count]
        count+=-1
    t=word+w
    print(t)

mirror("happy")
mirror("Python")
mirror("")
mirror("a")
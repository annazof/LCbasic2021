
count=0
def reverse(word):
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
    print(w)

reverse("happy")
reverse("Python")
reverse("")
reverse("a")

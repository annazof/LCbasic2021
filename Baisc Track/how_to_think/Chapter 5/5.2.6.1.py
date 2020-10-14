#We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function. Construct a
#small Python example to test whether this is possible, and write up your findings.

bob = ("Bob", "o")

def remove_letter(l, w):
    """
    Remove letter
    :param l: letter to be removed
    :param w: word
    :return: word with the letter
    """
    r=""
    for i in w:
        if i!=l:
            r+=i
    print(r)

remove_letter(bob[1],bob[0])

#Yes you can

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

remove_letter("a", "apple")
remove_letter("a", "banana")
remove_letter("z", "banana")
remove_letter("i", "Mississippi")
remove_letter("b", "")
remove_letter("b", "c")
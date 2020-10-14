
count=0
def is_palindrome(word):
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
    if w==word:
        print("TRUE")
    else:
        print("FALSE")

is_palindrome("abba")
is_palindrome("abab")
is_palindrome("tenet")
is_palindrome("banana")
is_palindrome("straw warts")
is_palindrome("a")
is_palindrome("")
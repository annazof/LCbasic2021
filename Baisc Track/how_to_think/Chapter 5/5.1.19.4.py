
def find(haystack, needle, start=0):
    for index,letter in enumerate(haystack[start:]):
        if letter == needle:
            return index + start
    return

print(find("banana", "n", 0))

#still requires work
#?????

def remove(substring, text):
    return print(text.replace(substring, "", 1))


remove("is", "Mississippi")
#== 2
remove("an", "banana")
#== 2
remove("ana", "banana")
#== 2
remove("nana", "banana")
#== 1
remove("nanan", "banana")
#== 0
remove("aaa", "aaaaaa")
#== 4
def remove_all(substring, text):
    return print(text.replace(substring, ""))

remove_all("an", "banana")
#== "ba"
remove_all("cyc", "bicycle") \
#== "bile"
remove_all("iss", "Mississippi")
#== "Mippi"
remove_all("eggs", "bicycle")
#== "bicycle"
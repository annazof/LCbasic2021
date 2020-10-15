
def returns_table_letters(s):
    letter_counts = {}
    s=s.lower()
    for letter in s:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] +=1
    return letter_counts

def print_letter_counts(letter_counts):
    for letter in sorted(letter_counts):
        print(letter, letter_counts[letter])


a= "ThiS is String with Upper and lower case Letters"

print_letter_counts(returns_table_letters(a))
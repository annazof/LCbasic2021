

def count_letters(word,letter):
    """
    Count letter in a word
    :param word: input word
    :param letter: input letter
    :return:
    """
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return (count)

print(count_letters("banana", "n"))





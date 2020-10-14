import string

def remove_punctuation(phrase,):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    x=len(phrase_sans_punct.split())
    count=0
    for word in phrase_sans_punct.split():
        if "e" in word:
            count +=1
    return(print("Your text contains", x ,"words, of which", count, "({0:.3f}".format(count/x*100), "%) contain an ""e""" ))

#Your text contains 243 words, of which 109 (44.8%) contain an "e".

text = """
And so even though we face the difficulties of today and tomorrow, I still have a dream. It is a dream deeply rooted in the American dream.
I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."
I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.
I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice.
I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.
I have a dream today!"""

remove_punctuation(text)



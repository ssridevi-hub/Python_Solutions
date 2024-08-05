# C-1.24 Write a short Python function that takes a strings,representing a sentence, and returns a copy 
# of the string with all punctuation removed. For example, if given the string "Let's try, Mike.", 
# this function would return "Lets try Mike".


def punctuation_remover(sentence):
    alphabets = list(chr(97+x) for x in range(0,26))
    t = ''

    for letter in sentence:
        if letter.lower() in alphabets or letter == " ":
            t += letter

    return t

print(punctuation_remover("My name is Sri, y email id : a@b.com"))
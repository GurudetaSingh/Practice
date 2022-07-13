# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
def pig_it(text):
    result = []
    words = text.split(' ')

    punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for word in words:
        if word in punc:
            result.append(word)
        else:
            sentence = word[1:] + word[0] + "ay"
            result.append(sentence)

    return " ".join(result)

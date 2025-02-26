def get_num_words(text):
    wordsplit = text.split()
    wordcount = 0
    for word in wordsplit:
        wordcount += 1
    return wordcount

def get_character_count(words):
    lowerwords = words.lower()
    wordsplit = lowerwords.split()
    characternumbers = {}
    for c in lowerwords:
        if c not in characternumbers:
            characternumbers[c] = 1
        else :
            characternumbers[c] += 1
    return characternumbers

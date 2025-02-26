def get_num_words(text):
    wordsplit = text.split()
    wordcount = 0
    for word in wordsplit:
        wordcount += 1
    return wordcount
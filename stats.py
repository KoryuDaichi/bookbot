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

def sort_on(dict):
    return dict["count"]

def character_count_to_sorted_list(charactercount):
    charactercountlist = []
    for char, count in charactercount.items():
        charactercountlist.append({"char": char, "count":count})
    charactercountlist.sort(key=lambda x: x["count"],reverse=True)
    return charactercountlist


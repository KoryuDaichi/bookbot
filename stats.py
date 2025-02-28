def get_num_words(text):
    wordsplit = text.split()
    return len(wordsplit)

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
        if char.isalpha():
            charactercountlist.append({"char": char, "count":count})
    charactercountlist.sort(key=sort_on,reverse=True)
    return charactercountlist


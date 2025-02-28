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

#def character_count_sort(charactercountlist):
#    charactercountlist.sort(key=sort_on,reverse=True)
#    return charactercountlist   

#test_dict = {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480}
#sorted_list = character_count_to_list(test_dict)
#print(sorted_list)
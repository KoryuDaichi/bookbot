def get_book_text(bookpath):
    book_contents = ""
    with open(bookpath) as f:
        book_contents = f.read()
    return book_contents

from stats import get_num_words
from stats import get_character_count
#from stats import character_count_sort
from stats import character_count_to_sorted_list


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    character_count = get_character_count(text)
    charactercountdictionary = character_count_to_sorted_list(character_count)
    print(charactercountdictionary)
    

main()
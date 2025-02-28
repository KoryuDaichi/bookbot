# Bookbot Main program

#open book from path
def get_book_text(bookpath):
    book_contents = ""
    with open(bookpath) as f:
        book_contents = f.read()
    return book_contents

#import functions from Stats.py
from stats import get_num_words
from stats import get_character_count
from stats import character_count_to_sorted_list


def main():
    #pull text from book into string called text.
    text = get_book_text("books/frankenstein.txt")
    #get the number of words in the text
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    #get and format Character count in text.
    character_count = get_character_count(text)
    charactercountdictionary = character_count_to_sorted_list(character_count)
    print(charactercountdictionary)
    

main()
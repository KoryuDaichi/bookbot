# main.py
# Bookbot Main program

# import the sys functionality
import sys

# import functions from Stats.py
from stats import get_num_words
from stats import get_character_count
from stats import character_count_to_sorted_list

# Initilization args
argument = sys.argv
if len(argument) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# open book from path
def get_book_text(bookpath):
    book_contents = ""
    with open(bookpath) as f:
        book_contents = f.read()
    return book_contents

def main():
    # pull the book path from the sys.argv list
    book = argument[1]
    # pull text from book into string called text.
    text = get_book_text(book)
    # get the number of words in the text
    num_words = get_num_words(text)
    # get and format Character count in text.
    character_count = get_character_count(text)
    charactercountdictionary = character_count_to_sorted_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in charactercountdictionary:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

main()
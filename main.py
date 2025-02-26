def get_book_text(bookpath):
    book_contents = ""
    with open(bookpath) as f:
        book_contents = f.read()
    return book_contents

from stats import get_num_words

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

main()
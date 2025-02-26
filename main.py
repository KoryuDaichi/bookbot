def get_book_text(bookpath):
    book_contents = ""
    with open(bookpath) as f:
        book_contents = f.read()
    return book_contents

def word_count(text):
    wordsplit = text.split()
    wordcount = 0
    for word in wordsplit:
        wordcount += 1
    return wordcount

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    print(f"{num_words} words found in the document")

main()
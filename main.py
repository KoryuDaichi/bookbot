def get_book_text(bookpath):
    book_contents = ""
    with open(bookpath) as f:
        book_contents = f.read()
    return book_contents


def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()
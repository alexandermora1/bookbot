def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def word_counter():
    book_text = get_book_text("books/frankenstein.txt")
    split_text = book_text.split()

    counter = 0
    for word in split_text:
        counter += 1

    print(f"{counter} words found in the document")
    return counter
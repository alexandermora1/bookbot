
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def word_counter(text):
    split_text = text.split()

    counter = 0
    for word in split_text:
        counter += 1

    print(f"{counter} words found in the document")
    return counter

def character_counter(text):
    lower_case = text.lower()

    count_chars = {}

    for char in lower_case:
        if char in count_chars:
            count_chars[char] += 1
        else:
            count_chars[char] = 1
    return count_chars
    
def sort_list(characters):
    new_dict_list = [
        {"char": key, "num": value}
        for key, value in characters.items()
    ]

    new_dict_list.sort(reverse=True, key=lambda x: x["num"])

    return new_dict_list
        
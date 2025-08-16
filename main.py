import sys
from stats import word_counter
from stats import get_book_text
from stats import character_counter
from stats import sort_list

def get_path():
  if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
  else:
      path = sys.argv[1]
  return path

def print_list(path, wordcount, dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")

def main():
    path = get_path()
    text = get_book_text(path)
    word_count = word_counter(text)
    characters = character_counter(text)
    dict_list = sort_list(characters)
    print_list(path, word_count, dict_list)

main()

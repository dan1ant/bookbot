import sys
from stats import get_num_words, get_characters_count, get_ordered_characters_count_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    characters_count = get_characters_count(book_text)
    characters_count_list = get_ordered_characters_count_list(characters_count)
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in characters_count_list:
        char, count = char_dict.values()
        print(f"{char}: {count}")
    print("============= END ===============")

main()

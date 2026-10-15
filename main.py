import sys
from stats import count, count_characters, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
           print("Usage: python3 main.py <path_to_book>")
           sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count(text)
    char_counts = count_characters(text)

    print_report(book_path, num_words,chars_dict_to_sorted_list(char_counts))



def print_report(book_path, num_words, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_counts:
        if not char[0].isalpha():
            continue

        print(f'{char[0]}: {char[1]}')

    print("============= END ===============")


main()

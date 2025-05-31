from stats import get_book_word_count
from stats import get_num_chars
from stats import sort_char_nums
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    word_count = get_book_word_count(file_path)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    num_chars = get_num_chars(file_path)
    #print(num_chars)
    #print(sort_char_nums(num_chars))
    for d in sort_char_nums(num_chars):
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

main()

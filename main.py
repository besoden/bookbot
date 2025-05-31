from stats import get_book_word_count
from stats import get_num_chars
from stats import sort_char_nums

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents    

def main(file_path):
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

main('books/frankenstein.txt')

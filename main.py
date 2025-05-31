from stats import get_book_word_count
from stats import get_num_chars

def get_book_text(file_path):
    #print("in get_book_text")
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents    

def main():
    #print("in main")
    # use get_book_text with the relative path to frankenstein.txt to print the text to console
    #file_contents = get_book_text('books/frankenstein.txt')
    #print(file_contents)
    word_count = get_book_word_count('books/frankenstein.txt')
    print(f"{word_count} words found in the document")
    num_chars = get_num_chars('books/frankenstein.txt')
    print(num_chars)

main()
#print("end of main.py")
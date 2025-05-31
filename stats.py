def get_book_word_count(file_path):
    #print("in get_book_word_count")
    with open(file_path) as f:
        file_contents = f.read()
    word_count = len(file_contents.split())
    return word_count